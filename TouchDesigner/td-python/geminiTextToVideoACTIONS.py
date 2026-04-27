from apiKeyActions import *
from geminiCompCallbacks import *
import geminiObjects
from geminiRequests import TextToVideoRequestObject
from geminiTerminalLogs import msg_formatter
import enumPars

request_engine = op("base_request_engine")
output_buffer = op("moviefilein1")
animation_channel = op("speed1")


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
    # set state of par for "Generating"
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", True)

    output_buffer.par.file = ""

    endpointInfo = resolveEndpointInfo()

    # resolve model
    # resolve model
    current_model: geminiObjects.GeminiModel = parent.geminiCOMP.ResolveModel()

    prompt = textOp.text

    # create input object
    geminiInput = geminiObjects.GeminiVideoInput()

    # add prompt
    geminiInput.addPromptInstance(prompt)

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
    request: TextToVideoRequestObject = TextToVideoRequestObject(
        geminiInput, output_buffer, model=current_model
    )

    def cleanup():
        smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)

    request.onDone = cleanup

    # make the request
    requestId = request_engine.MakeRequest(request, isPreview=current_model.isPreview)

    parent.geminiCOMP.par.Requestid = requestId
    msg_formatter(f"{parent.geminiCOMP.name} creating request")


def Generate(par: Par):
    """Generate new output on demand"""
    CreateRequest(parent.geminiCOMP.op("null_buffer"))


def Cancel(par: Par):
    """Generate new output on demand"""
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())


def Forcegenerate(par: Par):
    Cancel()
    run(Generate, delayFrames=10)


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


def Exportvideofile(par: Par):
    if parent.geminiCOMP.par.Hasvfs.eval():

        vfsFile: VFSFile = parent.geminiCOMP.vfs["temp.mp4"]

        # prompt user for target directory
        output_dir = ui.chooseFolder()
        if output_dir != "":
            # user selected a target directory
            vfsFile.export(output_dir)
            msg_formatter(f"Exporting video to file from {parent.geminiCOMP.name} VFS")


def Deletevideofile(par: Par):
    if parent.geminiCOMP.par.Hasvfs.eval():
        parent.geminiCOMP.op("moviefilein1").par.file = ""
        parent.geminiCOMP.vfs["temp.mp4"].destroy()
        msg_formatter(f"Removing video file from {parent.geminiCOMP.name} VFS")
