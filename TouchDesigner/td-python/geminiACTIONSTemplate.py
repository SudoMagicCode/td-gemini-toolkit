from apiKeyActions import *
import geminiObjects
from geminiRequests import TextToTextRequestObject
from geminiTerminalLogs import msg_formatter

request_engine = op("base_request_engine")


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
    request_engine.MakeRequest(request)
    msg_formatter(f"{parent.geminiCOMP.name} creating request")


def Generate(par: Par):
    """Generate new output on demand"""
    CreateRequest(op("null_buffer"))


def Cancel(par: Par):
    """Generate new output on demand"""
    CreateRequest(op("null_buffer"))
