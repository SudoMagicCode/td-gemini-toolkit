from apiKeyActions import *
import geminiObjects
from geminiRequests import ImageToVideoRequestObject
from geminiTerminalLogs import msg_formatter

request_engine = op("base_request_engine")
output_buffer = op("moviefilein1")
first = op("null_first_frame")
last = op("null_last_frame")


def OpCreated():
    msg_formatter(f"{parent.geminiCOMP.name} created")
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

    # create input object
    geminiInput = geminiObjects.GeminiVideoInput()

    prompt = dat.text

    promptInstance = geminiInput.addPromptInstance(prompt)
    promptInstance.addFirstFrame(first)
    # promptInstance.addLastFrame(last)

    # create a request object which resolves to the output_buffer
    request: ImageToVideoRequestObject = ImageToVideoRequestObject(
        geminiInput, output_buffer
    )

    # make the request
    requestId = request_engine.MakeRequest(request)
    parent.geminiCOMP.par.Requestid = requestId
    msg_formatter(f"{parent.geminiCOMP.name} creating request")


def Generate(par: Par):
    """Generate new output on demand"""
    CreateRequest(op("null_buffer"), op("null_first_frame"))


def Cancel(par: Par):
    """Generate new output on demand"""
    request_engine.CancelRequest(parent.geminiCOMP.par.Requestid.eval())
