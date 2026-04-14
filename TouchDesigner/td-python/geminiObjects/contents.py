from abc import ABC, abstractmethod

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

