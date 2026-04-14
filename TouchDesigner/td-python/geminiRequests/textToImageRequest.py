import json
from RequestBroker import RequestObjectBase
from geminiObjects import *

class TextToImageRequestObject(RequestObjectBase):
	def __init__(self, input: GeminiInputContent):
		data = input.renderContents()
		data_string = json.dumps(data)
		super().__init__(bytes(data_string))

		self._url = CreateEndpoint(Model.GEMINI_3_FLASH_PREVIEW, Operation.GENERATE_CONTENT)
		self._method = "POST"
		self._header = {
    		"Content-Type": "application/json"
		}

	def resolve(self, result:bytes):
		print(str(result))


	def error(self, error):
		return super().error(error)