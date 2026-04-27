from apiKeyActions import *
from geminiCompCallbacks import *
import geminiObjects
from geminiRequests import ImageTextToImageRequestObject
from geminiTerminalLogs import msg_formatter
import enumPars

request_engine = op("base_request_engine")
output_buffer = op("script1")


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

    # resolve model
    endpointInfo = resolveEndpointInfo()
    modelType = endpointInfo.get("modelType")
    if modelType == "studio":
        model_par_enum = enumPars.StudioImageModels[parent.geminiCOMP.par.Model.eval()]
    else:
        model_par_enum = enumPars.VertexImageModels[parent.geminiCOMP.par.Model.eval()]

    currentModel: geminiObjects.GeminiModel = model_par_enum.value.model.value

    # grab text from buffer
    textPart = geminiObjects.Adaptors.DATtoGeminiTextPart(dat)
    imagePart = geminiObjects.Adaptors.TOPtoGeminiImagePart(top)

    # create input object
    geminiInput = geminiObjects.GeminiInput()
    userContent = geminiInput.addUserContent()

    # add a text part to the contents
    userContent.addPart(imagePart)
    userContent.addPart(textPart)

    # setup generation config
    config = geminiInput.addGenerationConfig()

    if parent.geminiCOMP.par.Useinput.eval() == False:
        # create additional image config info
        imageConfig = config.AddImageConfig()

        resolution = geminiObjects.GenerationImageSize[
            parent.geminiCOMP.par.Resolution.eval()
        ]
        aspect = geminiObjects.GenerationAspectRatio[
            parent.geminiCOMP.par.Aspectratio.eval()
        ]
        # additional attributes

        imageConfig.SetAspect(aspect)
        imageConfig.SetImageSize(resolution)

    # create a request object which resolves to the output_buffer
    request = ImageTextToImageRequestObject(
        geminiInput, output_buffer, model=currentModel
    )

    def cleanup():
        smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)

    request.onDone = cleanup

    # make the request
    requestId = request_engine.MakeRequest(request, isPreview=currentModel.isPreview)

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


def Forcegenerate(par: Par):
    Cancel()
    run(Generate, delayFrames=10)


def Saveimage(par: Par):
    destination = ui.chooseFile(
        load=False, fileTypes=tdu.fileTypes["image"], title="Save image as"
    )
    if destination == None:
        pass
    else:
        source: TOP = parent.geminiCOMP.op("out_response")
        source.save(destination)
