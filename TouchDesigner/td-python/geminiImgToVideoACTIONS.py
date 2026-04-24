from apiKeyActions import *
import geminiObjects
from geminiRequests import ImageToVideoRequestObject
from geminiTerminalLogs import msg_formatter
import enumPars

request_engine = op("base_request_engine")
output_buffer = op("moviefilein1")
first = op("null_first_frame")
animation_channel = op("speed1")


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
        createRequest(textOp, top)


def createRequest(dat: textDAT, top: TOP):

    # set state of par for "Generating"
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", True)

    output_buffer.par.file = ""

    veo_model_par_enum = enumPars.VeoModels[parent.geminiCOMP.par.Model.eval()]
    model: geminiObjects.GeminiModel = veo_model_par_enum.value.model
    isPreview: bool = model.isPreview

    prompt = dat.text

    # create input object
    geminiInput = geminiObjects.GeminiVideoInput()
    promptInstance = geminiInput.addPromptInstance(prompt)
    promptInstance.addFirstFrame(first)

    # pull additional parameters
    resolution = geminiObjects.VeoParameterResolution[
        parent.geminiCOMP.par.Resolution.eval()
    ]
    aspect = geminiObjects.VeoParameterAspectRatio[
        parent.geminiCOMP.par.Aspectratio.eval()
    ]
    duration = geminiObjects.VeoParameterDuration[
        parent.geminiCOMP.par.Videolength.eval()
    ]

    # add pars to config
    config = geminiInput.addParameters()
    config.setAspect(aspect)
    config.setResolution(resolution)
    config.setDuration(duration)

    # create a request object which resolves to the output_buffer
    request: ImageToVideoRequestObject = ImageToVideoRequestObject(
        geminiInput, output_buffer, model=model
    )

    def cleanup():
        smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)

    request.onDone = cleanup

    # make the request
    requestId = request_engine.MakeRequest(request, isPreview=isPreview)

    parent.geminiCOMP.par.Requestid = requestId
    msg_formatter(f"{parent.geminiCOMP.name} creating request")

    # set state of par for "Generating"
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", True)


def Generate(par: Par):
    """Generate new output on demand"""
    CreateRequest(op("null_buffer"), op("null_first_frame"))


def Cancel(par: Par):
    """Generate new output on demand"""
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())


def resolutionFromPars() -> tuple[int, int]:
    resolutionMap = {
        geminiObjects.VeoParameterResolution.RESOLUTION_4k: (3840, 2160),
        geminiObjects.VeoParameterResolution.RESOLUTION_1080p: (1920, 1080),
        geminiObjects.VeoParameterResolution.RESOLUTION_720p: (1280, 720),
    }

    resolution = geminiObjects.VeoParameterResolution[
        parent.geminiCOMP.par.Resolution.eval()
    ]
    aspect = geminiObjects.VeoParameterAspectRatio[
        parent.geminiCOMP.par.Aspectratio.eval()
    ]

    aspectValue = aspect.value

    match aspectValue:
        case "16:9":
            x, y = resolutionMap[resolution][0], resolutionMap[resolution][1]
        case _:
            x, y = resolutionMap[resolution][1], resolutionMap[resolution][0]

    resolution = (x, y)
    return resolution
