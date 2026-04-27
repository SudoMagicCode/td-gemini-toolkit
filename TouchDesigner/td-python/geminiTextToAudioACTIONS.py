from apiKeyActions import *
from geminiCompCallbacks import *
import geminiObjects
from geminiRequests import TextToAudioRequest
from geminiTerminalLogs import msg_formatter
import enumPars

request_engine = op("base_request_engine")
output_buffer = op("audiofilein1")
img_input_buffer = op("null_image_buffer")


def OpCreated():
    msg_formatter(f"{parent.geminiCOMP.name} created")
    resolveApiKeyServer()
    pass


def onExit():
    pass


def CreateRequest(textOp: DAT, top: TOP):
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


def createRequest(textOp: DAT, top: TOP):
    textPart = geminiObjects.Adaptors.DATtoGeminiTextPart(textOp)
    geminiInput = geminiObjects.GeminiInput()
    userContent = geminiInput.addUserContent()

    # resolve model
    current_model: geminiObjects.GeminiModel = parent.geminiCOMP.ResolveModel()

    # add a text part to the contents
    userContent.addPart(textPart)

    # include image if user has enabled parameter
    if parent.geminiCOMP.par.Includeimage.eval():
        imagePart = geminiObjects.Adaptors.TOPtoGeminiImagePart(top)
        userContent.addPart(imagePart)

    # create a request object which resolves to the output_buffer
    request = TextToAudioRequest(geminiInput, output_buffer, model=current_model)

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
    CreateRequest(op("null_buffer"), img_input_buffer)


def Cancel(par: Par):
    """Generate new output on demand"""
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())


def Forcegenerate(par: Par):
    Cancel(parent.geminiCOMP.par.Cancel)

    def runGenerate():
        Generate(parent.geminiCOMP.par.Generate)

    run(runGenerate, delayFrames=10)


def Deleteaudiofile(par: Par):
    msg_formatter(f"Removing audio file from {parent.geminiCOMP.name} VFS")
    if parent.geminiCOMP.par.File.eval() != "":
        parent.geminiCOMP.par.File = ""
        parent.geminiCOMP.vfs["temp.mp3"].destroy()


def Exportaudiofile(par: Par):
    """Export audio file from VFS"""
    # ensure we have a file to export
    if parent.geminiCOMP.par.File.eval() != "":

        vfsFile: VFSFile = parent.geminiCOMP.vfs["temp.mp3"]

        # prompt user for target directory
        output_dir = ui.chooseFolder()
        if output_dir != "":
            # user selected a target directory
            vfsFile.export(output_dir)
