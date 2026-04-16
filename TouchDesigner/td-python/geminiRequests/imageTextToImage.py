import json
import base64

from RequestBroker import RequestObjectBase
from geminiObjects import *

class TextToImageRequestObject(RequestObjectBase):
	def __init__(self, input: GeminiInputContent, output:scriptTOP):
		data = input.renderContents()
		data_string = json.dumps(data)
		super().__init__(data_string)

		self._output = output

		self._url = CreateEndpoint(Model.GEMINI_3_FLASH_PREVIEW, Operation.GENERATE_CONTENT)
		self._method = "POST"
		self._header = {
    		"Content-Type": "application/json"
		}

	def resolve(self, result:bytes):
		text = result.decode("utf-8", errors="ignore")

		output = GeminiOutput.fromJson(text)
		for candidate in output.candidates:
			for part in candidate.content.parts:
				if len(part.data)>0:
					img_bytes = base64.b64decode(part.data)
					self._output.store("image_data", img_bytes)
					self._output.store("mime", ".jpg")

		self._output.store("metadata", output.usage_metadata)


	def error(self, error):
		return super().error(error)