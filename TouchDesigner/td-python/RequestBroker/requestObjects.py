import json
from requestObjectBase import RequestObjectBase
from geminiObjects import *

class TextToTextRequestObject(RequestObjectBase):
	def __init__(self, input: GeminiInputContent):
		data = input.renderContents()
		data_string = json.dumps(data)
		print(data_string)
		super().__init__(data_string)
		
		self._url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent'
		self._method = "POST"
		self._header = {
    		"Content-Type": "application/json"
		}

	def resolve(self, result:bytes):
		text = result.decode("utf-8", errors="ignore")
		print(text)

	def error(self, error):
		return super().error(error)
	

class TextToImageRequestObject(RequestObjectBase):
	def __init__(self, input: GeminiInputContent):
		data = input.renderContents()
		data_string = json.dumps(data)
		super().__init__(bytes(data_string))

		self._url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent'
		self._method = "POST"
		self._header = {
    		"Content-Type": "application/json"
		}

	def resolve(self, result:bytes):
		print(str(result))


	def error(self, error):
		return super().error(error)
