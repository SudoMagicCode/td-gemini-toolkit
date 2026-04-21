from apiKeyActions import *
import geminiObjects
from geminiRequests import TextToVideoRequestObject
from geminiTerminalLogs import msg_formatter

request_engine = op("base_request_engine")
output_buffer = op("moviefilein1")


def OpCreated():
    msg_formatter(f"{parent.geminiCOMP.name} created")
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

    op("moviefilein1").par.file = ""
    op("timer1").par.start.pulse()

    # create input object
    geminiInput = geminiObjects.GeminiVideoInput()

    prompt = textOp.text

    geminiInput.addPromptInstance(prompt)

    # create a request object which resolves to the output_buffer
    request: TextToVideoRequestObject = TextToVideoRequestObject(
        geminiInput, output_buffer
    )

    # make the request
    requestId = request_engine.MakeRequest(request)
    parent.geminiCOMP.par.Requestid = requestId
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


def Generate(par: Par):
    """Generate new output on demand"""
    CreateRequest(op("null_buffer"))


def Cancel(par: Par):
    """Generate new output on demand"""
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())
    smOpUtils.set_par_state(parent.geminiCOMP, "Generating", False)
