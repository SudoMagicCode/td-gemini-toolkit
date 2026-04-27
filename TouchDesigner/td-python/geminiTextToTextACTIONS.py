from apiKeyActions import *
from geminiCompCallbacks import *
import geminiObjects
from geminiRequests import TextToTextRequestObject
from geminiTerminalLogs import msg_formatter
import enumPars

request_engine = op("base_request_engine")
output_buffer = op("text_output_buffer")


def OpCreated():
    msg_formatter(f"{parent.geminiCOMP.name} created")
    resolveApiKeyServer()
    pass


def onExit():
    pass


def CreateRequest(textOp: textDAT):
    """Gate against requests when there's currently one in progress"""
    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping"
        )
    else:
        if textOp.text == "":
            msg_formatter(f"WARN {parent.geminiCOMP.name} prompt is empty, skipping")
        else:
            createRequest(textOp=textOp)


def createRequest(textOp: textDAT):
    # resolve model
    current_model: geminiObjects.GeminiModel = parent.geminiCOMP.ResolveModel()

    # grab text from buffer
    textPart = geminiObjects.Adaptors.DATtoGeminiTextPart(textOp)

    # create input object
    geminiInput = geminiObjects.GeminiInput()
    userContent = geminiInput.addUserContent()

    # add a text part to the contents
    userContent.addPart(textPart)

    # create a request object which resolves to the output_buffer
    request = TextToTextRequestObject(geminiInput, output_buffer, model=current_model)

    def cleanup():
        smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)

    request.onDone = cleanup

    # make the request
    requestId = request_engine.MakeRequest(request, isPreview=current_model.isPreview)

    parent.geminiCOMP.par.Requestid = requestId
    msg_formatter(f"{parent.geminiCOMP.name} creating request")

    # set state of par for "Generating"
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", True)


def Generate(par: Par):
    """Generate new output on demand"""
    CreateRequest(op("null_buffer"))


def Cancel(par: Par):
    """Cancel running request"""
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())


def Forcegenerate(par: Par):
    Cancel(parent.geminiCOMP.par.Cancel)

    def runGenerate():
        Generate(parent.geminiCOMP.par.Generate)

    run(runGenerate, delayFrames=10)
