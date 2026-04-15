from apiKeyActions import *
from geminiObjects import GeminiInputContent
from geminiRequests import TextToTextRequestObject
from geminiTerminalLogs import msg_formatter

request_engine = op('base_request_engine')
output_buffer = op('text_output_buffer')


def CreateRequest(textOp: textDAT):
    '''Gate against requests when there's currently one in progress
    '''
    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping")
    else:
        createRequest(textOp=textOp)


def createRequest(textOp: textDAT):
    # grab text from buffer
    input_text = textOp.text

    # create input object
    inputContent = GeminiInputContent()

    # add a text part to the contents
    inputContent.addTextPart(input_text)

    # create a request object which resolves to the output_buffer
    request = TextToTextRequestObject(inputContent, output_buffer)

    # make the request
    request_engine.MakeRequest(request)
    msg_formatter(f"{parent.geminiCOMP.name} creating request")


def Generatenew(par: Par):
    '''Generate new output on demand
    '''
    CreateRequest(op('null_buffer'))
