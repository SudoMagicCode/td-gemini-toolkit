from apiKeyActions import *
import geminiObjects
from geminiRequests import TextToTextRequestObject
from geminiTerminalLogs import msg_formatter

request_engine = op("base_request_engine")


def OpCreated():
    msg_formatter(f"{parent.geminiCOMP.name} created")
    pass


def onExit():
    pass


def CreateRequest():
    """Gate against requests when there's currently one in progress"""
    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping"
        )
    else:
        createRequest()


def createRequest():

    # create a request object which resolves to the output_buffer
    request: callable

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
