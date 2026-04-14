import json
from RequestBroker import RequestObjectBase
from geminiObjects import *

class TextToTextRequestObject(RequestObjectBase):
	def __init__(self, input: GeminiInputContent):
		data = input.renderContents()
		data_string = json.dumps(data)
		print(data_string)
		super().__init__(data_string)
		
		self._url = CreateEndpoint(Model.GEMINI_3_1_FLASH_PREVIEW, Operation.GENERATE_CONTENT)
		self._method = "POST"
		self._header = {
    		"Content-Type": "application/json"
		}

	def resolve(self, result:bytes):
		text = result.decode("utf-8", errors="ignore")
		print(text)

	def error(self, error):
		return super().error(error)