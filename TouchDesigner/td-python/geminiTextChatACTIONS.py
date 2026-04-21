from apiKeyActions import *
import geminiObjects
from geminiRequests import TextToTextRequestObject
from geminiTerminalLogs import msg_formatter

request_engine = op("base_request_engine")
output_buffer = op("text_output_buffer")


def CreateRequest(textOp: textDAT):
    """Gate against requests when there's currently one in progress"""
    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping"
        )
    else:
        createRequest(textOp=textOp)


def createRequest(textOp: textDAT):
    # grab text from buffer
    textPart = geminiObjects.Adaptors.DATtoGeminiTextPart(textOp)

    # create input object
    geminiInput = geminiObjects.GeminiInput()
    userContent = geminiInput.addUserContent()

    # add a text part to the contents
    userContent.addPart(textPart)

    # create a request object which resolves to the output_buffer
    request = TextToTextRequestObject(userContent, output_buffer)

    # make the request
    request_engine.MakeRequest(request)
    msg_formatter(f"{parent.geminiCOMP.name} creating request")

    # set state of par for "Generating"
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", True)

    # NOTE this is just a placeholder until there's a way to run a callback
    run(
        smOpUtils.set_par_state,
        parent.geminiCOMP,
        "Generating",
        False,
        delayFrames=200,
    )


def Generatenew(par: Par):
    """Generate new output on demand"""
    CreateRequest(op("null_buffer"))
