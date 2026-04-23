from apiKeyActions import *
import geminiObjects
from geminiRequests import AudioToTextRequest
from geminiTerminalLogs import msg_formatter
import uuid

current_model = geminiObjects.Model.GEMINI_3_FLASH_PREVIEW
request_engine = op("base_request_engine")
output_buffer = op("text_output_buffer")
timeout_timer = op("timer_audio_timeout")


def OpCreated():
    msg_formatter(f"{parent.geminiCOMP.name} created")
    parent.geminiCOMP.par.Record = False
    parent.geminiCOMP.par.Tempfile = ""
    resolveApiKeyServer()
    pass


def onExit():
    pass


def resolveCurrentModel() -> str:
    return current_model.value.split("/")[1]


def CreateRequest(path: str, textOp: DAT):
    """Gate against requests when there's currently one in progress"""
    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping"
        )
    else:
        createRequest(path, textOp)


def createRequest(path: str, textOp: DAT):
    textPart = geminiObjects.Adaptors.DATtoGeminiTextPart(textOp)
    audioPart = geminiObjects.Adaptors.FiletoGeminiAudioPart(path, "audio/wav")

    # create input object
    geminiInput = geminiObjects.GeminiInput()
    userContent = geminiInput.addUserContent()

    # add a text part to the contents
    userContent.addPart(textPart)
    userContent.addPart(audioPart)

    # create a request object which resolves to the output_buffer
    request = AudioToTextRequest(geminiInput, output_buffer, model=current_model)

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
    if parent.geminiCOMP.par.Usesourcefile.eval():
        path = parent.geminiCOMP.par.Sourcefile.eval()
    else:
        if parent.geminiCOMP.par.Tempfile.eval() != "":
            path = parent.geminiCOMP.par.Tempfile.eval()
        else:
            msg_formatter(
                f"WARN {parent.geminiCOMP.name} has no temp file, please record something first"
            )
            return

    CreateRequest(path, op("null_buffer"))


def Cancel(par: Par):
    """Generate new output on demand"""
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())


def Record(par: Par):
    if par.eval():
        path = f"{app.tempFolder}/{uuid.uuid4()}.wav"
        parent.geminiCOMP.par.Tempfile = path
        op("audiofileout1").par.record = 1
        timeout_timer.par.start.pulse()

    else:
        op("audiofileout1").par.record = 0
        # if autogenerate is on let's submit our recorded files right away
        if parent.geminiCOMP.par.Autogenerate.eval():
            run(Generate, parent.geminiCOMP.par.Generate, delayFrames=10)
