from apiKeyActions import *
from geminiCompCallbacks import *
import geminiObjects
from geminiRequests import ChatRequestObject
from geminiTerminalLogs import msg_formatter
import enumPars

request_engine = op("base_request_engine")


def OpCreated():
    msg_formatter(f"{parent.geminiCOMP.name} created")
    resolveApiKeyServer()
    pass


def onExit():
    pass


def CreateRequest(
    fifo: fifoDAT, newEntry: str, role: str = "user", context: DAT = op("null_context")
):
    """Gate against requests when there's currently one in progress"""

    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping"
        )
    else:
        # add new entry to fifo
        fifo.appendRow([role, newEntry])
        createRequest(fifo, context)


def createRequest(fifo: fifoDAT, context: DAT):
    info = resolveEndpointInfo()
    if info.get("modelType") == "studio":
        current_model = geminiObjects.StudioModels[parent.geminiCOMP.par.Model.eval()]
    else:
        current_model = geminiObjects.VertexModels[parent.geminiCOMP.par.Model.eval()]

    # create input object
    geminiInput = geminiObjects.GeminiInput()

    contents = geminiObjects.Adaptors.FIFODattoGeminiContents(context)
    geminiInput.addContent(contents)
    print(type(current_model.value))
    # create a request object which resolves to the output_buffer
    request = ChatRequestObject(geminiInput, fifo, model=current_model.value)

    def cleanup():
        smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)

    request.onDone = cleanup

    # make the request
    requestId = request_engine.MakeRequest(
        request, isPreview=current_model.value.isPreview
    )

    parent.geminiCOMP.par.Requestid = requestId
    msg_formatter(f"{parent.geminiCOMP.name} creating request")

    # set state of par for "Generating"
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", True)


def Generate(par: Par):
    """Generate new output on demand"""
    text = op("null_buffer").text
    role = "user"
    CreateRequest(op("fifo1"), text, role)


def Cancel(par: Par):
    """Cancel running request"""
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())
