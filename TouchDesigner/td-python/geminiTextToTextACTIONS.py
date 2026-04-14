from apiKeyActions import *
from geminiObjects import GeminiInputContent
from geminiRequests import TextToTextRequestObject

request_engine = op('base_request_engine') 
output_buffer = op('text_output_buffer')

def CreateRequest(textOp:textDAT):
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