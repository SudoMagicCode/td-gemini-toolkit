from abc import ABC, abstractmethod
import json


class GeminiContentPart(ABC):
	@abstractmethod
	def renderPart(self)->dict:
		raise Exception("unimplemented")

class GeminiContentTextPart(GeminiContentPart):
	def __init__(self, text:str):
		self._text = text
	
	def renderPart(self)->dict:
		return {"text": self._text}

class GeminiInputContent:
	def __init__(self):
		self._parts:list[GeminiContentPart] = []
	
	def renderContents(self)->dict:
		partData = [p.renderPart() for p in self._parts]
		return {"contents":{"parts": partData } }

	def addTextPart(self, text:str):
		newPart = GeminiContentTextPart(text)
		self._parts.append(newPart)




class GeminiOutputPart:
	def __init__(self, input:dict):
		self.text = input["text"]
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
		self.thoughts_token_count = input['thoughtsTokenCount']
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