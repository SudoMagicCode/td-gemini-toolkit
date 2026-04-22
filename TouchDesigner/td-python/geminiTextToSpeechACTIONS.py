from apiKeyActions import *
import geminiObjects
from geminiRequests import TextToSpeechRequest
from geminiTerminalLogs import msg_formatter

request_engine = op("base_request_engine")
output_buffer = op("audiofilein1")


def OpCreated():
    msg_formatter(f"{parent.geminiCOMP.name} created")
    resolveApiKeyServer()
    pass


def onExit():
    pass


def CreateRequest(textOp: DAT):
    """Gate against requests when there's currently one in progress"""
    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping"
        )
    else:
        createRequest(textOp)


def createRequest(textOp: DAT):

    # grab text from buffer
    textPart = geminiObjects.Adaptors.DATtoGeminiTextPart(textOp)

    # create input object
    geminiInput = geminiObjects.GeminiInput()
    userContent = geminiInput.addUserContent()

    # add a text part to the contents
    userContent.addPart(textPart)

    config = geminiInput.addGenerationConfig()
    speechConfig = config.AddSpeechConfig()
    speechConfig.SetPrebuiltVoice(geminiObjects.TTSVoiceName.KORE)

    # create a request object which resolves to the output_buffer
    request = TextToSpeechRequest(geminiInput, output_buffer)

    def cleanup():
        smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)

    request.onDone = cleanup

    # make the request
    requestId = request_engine.MakeRequest(request)
    parent.geminiCOMP.par.Requestid = requestId
    msg_formatter(f"{parent.geminiCOMP.name} creating request")

    # set state of par for "Generating"
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", True)


def Generate(par: Par):
    """Generate new output on demand"""
    CreateRequest(op("null_buffer"))


def Cancel(par: Par):
    """Generate new output on demand"""
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())
