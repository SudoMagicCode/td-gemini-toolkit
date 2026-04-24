from apiKeyActions import *
import geminiObjects
from geminiRequests import *
from geminiTerminalLogs import msg_formatter

request_engine = op("base_request_engine")
output_buffer = op("text_output_buffer")


def OpCreated():
    msg_formatter(f"{parent.geminiCOMP.name} created")
    resolveApiKeyServer()
    pass


def onExit():
    pass


def CreateRequest(textOp: textDAT, top: TOP):
    """Gate against requests when there's currently one in progress"""
    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping"
        )
    else:
        if textOp.text == "":
            msg_formatter(f"WARN {parent.geminiCOMP.name} prompt is empty, skipping")
        else:
            createRequest(textOp, top)


def createRequest(dat: textDAT, top: TOP):
    info = resolveEndpointInfo()
    if info.get("modelType") == "studio":
        current_model = geminiObjects.StudioModels[parent.geminiCOMP.par.Model.eval()]
    else:
        current_model = geminiObjects.VertexModels[parent.geminiCOMP.par.Model.eval()]

    # grab text from buffer
    textPart = geminiObjects.Adaptors.DATtoGeminiTextPart(dat)
    imagePart = geminiObjects.Adaptors.TOPtoGeminiImagePart(top)

    # create input object
    geminiInput = geminiObjects.GeminiInput()
    userContent = geminiInput.addUserContent()

    # add parts to the contents
    userContent.addPart(imagePart)
    userContent.addPart(textPart)

    # create a request object which resolves to the output_buffer
    request = ImageTextToTextRequestObject(
        geminiInput, output_buffer, model=current_model.value
    )

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
    CreateRequest(op("null_text_buffer"), op("null_image_buffer"))


def Cancel(par: Par):
    """Cancel running request"""
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())
