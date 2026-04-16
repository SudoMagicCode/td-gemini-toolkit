from abc import ABC, abstractmethod
import json
import base64

class GeminiContentPart(ABC):
	@abstractmethod
	def renderPart(self)->dict:
		raise Exception("unimplemented")

class GeminiContentTextPart(GeminiContentPart):
	def __init__(self, text:str):
		self._text = text
		self._role = ""
	
	def renderPart(self)->dict:
		part = { "text": self._text }
		return part
	
class GeminiContentImagePart(GeminiContentPart):
	def __init__(self, mime_type:str, image_bytes:bytes):
		self._mime_type = mime_type
		self._data = base64.b64encode(image_bytes).decode('utf-8')
	
	def renderPart(self)->dict:
		return {"inline_data": {
			"mime_type": self._mime_type,
			"data": self._data
		}}

class GeminiContent:
	def __init__(self, role:str):
		self._parts:list[GeminiContentPart] = []
		self._role = role

	def renderContents(self)->dict:
		contentsData = [p.renderPart() for p in self._parts]
		content = { "role": self._role,
					"parts":contentsData }
		return content

	def addPart(self, part:GeminiContentPart):
		self._parts.append(part)

	def addTextPart(self, text:str):
		newPart = GeminiContentTextPart(text)
		self.addPart(newPart)

	def addImagePart(self, mime_type:str, image_bytes:bytes):
		newPart = GeminiContentImagePart(mime_type, image_bytes)
		self.addPart(newPart)



class GeminiInput:
	def __init__(self):
		self._contents:list[GeminiContent] = []
	
	def render(self)->dict:
		contents = [c.renderContents() for c in self._contents]
		return { "contents": contents }
	
	def addUserContent(self) -> GeminiContent:
		c = GeminiContent("user")
		self._contents.append(c)
		return c
	
	def addModelContent(self) -> GeminiContent:
		c = GeminiContent("model")
		self._contents.append(c)
		return c





class GeminiOutputPart:
	def __init__(self, input:dict):

		self.text = None
		self.inline_data = None
		self.mime_type = None
		self.data = None

		if "text" in input:
			self.text = input["text"]
		
		if "inlineData" in input:
			self.inline_data = input["inlineData"]
			self.mime_type = input["inlineData"]["mimeType"] 
			self.data = input["inlineData"]["data"]

		self.thought_signature = input["thoughtSignature"]
		pass

class GeminiOutputContent:
	def __init__(self, input:dict):
		self.parts = [GeminiOutputPart(p) for p in input["parts"]]
		self.role = input["role"]
		pass

class GeminiCandidate:
	def __init__(self, input:dict):
		self.content = GeminiOutputContent(input["content"])
		self.finish_reason = input["finishReason"]
		self.index = input["index"]
		pass

class GeminiUsageMetadata:
	def __init__(self, input:dict):
		self.prompt_token_count = input['promptTokenCount']
		self.candidates_token_count = input['candidatesTokenCount']
		self.total_token_count = input['totalTokenCount']
		self.prompt_tokens_details = input['promptTokensDetails']
		#self.thoughts_token_count = input['thoughtsTokenCount']
		pass


class GeminiOutput:
	def __init__(self, input:dict):
		self.model_version = input['modelVersion']
		self.response_id = input['responseId']
		self.usage_metadata = GeminiUsageMetadata(input['usageMetadata'])
		self.candidates = [GeminiCandidate(c) for c in input['candidates']]
		pass

	@classmethod
	def fromJson(cls, json_str:str):
		data = json.loads(json_str)
		return cls(data)