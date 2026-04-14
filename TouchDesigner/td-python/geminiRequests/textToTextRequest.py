import json
from RequestBroker import RequestObjectBase
from geminiObjects import *

class TextToTextRequestObject(RequestObjectBase):
	def __init__(self, input: GeminiInputContent, outputOp:textDAT):
		data = input.renderContents()
		data_string = json.dumps(data)
		super().__init__(data_string)
		
		self._output = outputOp
		
		self._url = CreateEndpoint(Model.GEMINI_3_FLASH_PREVIEW, Operation.GENERATE_CONTENT)
		self._method = "POST"
		self._header = {
    		"Content-Type": "application/json"
		}

	def resolve(self, result:bytes):
		text = result.decode("utf-8", errors="ignore")
		self._output.text = text

	def error(self, error):
		return super().error(error)