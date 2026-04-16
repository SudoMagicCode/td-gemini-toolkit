from apiKeyActions import *
import geminiObjects 
from geminiRequests import ImageTextToImageRequestObject
from geminiTerminalLogs import msg_formatter

request_engine = op('base_request_engine')
output_buffer = op('script1')


def CreateRequest(textOp: textDAT, top:TOP):
    '''Gate against requests when there's currently one in progress
    '''
    if parent.geminiCOMP.par.Generating.eval():
        msg_formatter(
            f"WARN {parent.geminiCOMP.name} is currently generating text, skipping")
    else:
        createRequest(textOp, top)


def createRequest(dat: textDAT, top:TOP):
    # grab text from buffer
    textPart = geminiObjects.Adaptors.DATtoGeminiTextPart(dat)
    imagePart = geminiObjects.Adaptors.TOPtoGeminiImagePart(top)

    # create input object
    inputContent = geminiObjects.GeminiInputContent()

    # add a text part to the contents
    inputContent.addPart(imagePart)
    inputContent.addPart(textPart)

    # additional attributes
    resolution = parent.geminiCOMP.par.Resolution.eval()
    aspect = parent.geminiCOMP.par.Aspectratio.eval()
    
    # debug pars
    debug(resolution, aspect)
    
    # create a request object which resolves to the output_buffer
    request = ImageTextToImageRequestObject(inputContent, output_buffer)

    # make the request
    request_engine.MakeRequest(request)
    msg_formatter(f"{parent.geminiCOMP.name} creating request")


def Generatenew(par: Par):
    '''Generate new output on demand
    '''
    CreateRequest(op('null_text_buffer'), op('null_image_buffer'))
