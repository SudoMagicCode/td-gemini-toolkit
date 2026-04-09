import json
from requestObjectBase import RequestObjectBase
from geminiObjects import *

class TextToTextRequestObject(RequestObjectBase):
	def __init__(self, input: GeminiInputContent):
		data = input.renderContents()
		data_string = json.dumps(data)
		super().__init__(bytes(data_string))

	def resolve(self, result):
		print(str(result))

	def error(self, error):
		return super().error(error)
	

class TextToImageRequestObject(RequestObjectBase):
	def __init__(self, input: GeminiInputContent):
		data = input.renderContents()
		data_string = json.dumps(data)
		super().__init__(bytes(data_string))

	def resolve(self, result):
		print(str(result))


	def error(self, error):
		return super().error(error)
