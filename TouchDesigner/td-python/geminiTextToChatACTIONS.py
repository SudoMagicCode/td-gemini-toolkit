from apiKeyActions import *
import geminiObjects
from geminiRequests import ChatRequestObject
from geminiTerminalLogs import msg_formatter

request_engine = op('base_request_engine')


def CreateRequest(fifo: fifoDAT, newEntry: str, role: str = "user"):
    '''Gate against requests when there's currently one in progress
    '''

    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping")
    else:
        # add new entry to fifo
        fifo.appendRow([role, newEntry])
        createRequest(fifo)


def createRequest(fifo: fifoDAT):
    # grab text from buffer
    print('creating request')
    # create input object
    geminiInput = geminiObjects.GeminiInput()

    contents = geminiObjects.Adaptors.FIFODattoGeminiContents(fifo)
    geminiInput.addContent(contents)

    # create a request object which resolves to the output_buffer
    request = ChatRequestObject(geminiInput, fifo)

    # make the request
    print('making request')
    request_engine.MakeRequest(request)
    msg_formatter(f"{parent.geminiCOMP.name} creating request")


def Generate(par: Par):
    '''Generate new output on demand
    '''
    text = parent.geminiCOMP.par.Defaultprompt.eval()
    role = "user"
    CreateRequest(op('fifo1'), text, role)


def Cancel(par: Par):
    '''Cancel running request'''
    request_engine.CancelRequest()
