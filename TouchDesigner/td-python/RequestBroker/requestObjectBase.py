from typing import Dict, Any, runtime_checkable
from abc import ABC, abstractmethod


class RequestObjectBase(ABC):
	def __init__(self, input:bytes):
		self._inputData = input
		self._status: dict[str, Any] = {}
		self._completed = False
		self._result:bytes = b""

	def _resolve(self, statusCode: Dict[str, Any], headerDict: Dict[str, str], data:bytes=None):
		self._result = data
		self._status = statusCode
		self._headerDict = headerDict
		self._completed = True
		self.resolve(self._result)

	def _error(self, error:Exception):
		self._completed = True
		self.error(error)

	def isCompleted(self)->bool:
		return self._completed

	def input(self)->bytes:
		return self._inputData

	def result(self)->bytes:
		if not self._completed:
			raise Exception("Request is incomplete")
		return self._result

	def statusCode(self)->int:
		if not self._completed:
			raise Exception("Request is incomplete")
		return self._status["code"]
	
	def statusMessage(self)->str:
		if not self._completed:
			raise Exception("Request is incomplete")
		return self._status["message"]

	@abstractmethod
	def resolve(self, result:bytes):
		raise Exception("Unimplemented")
	
	@abstractmethod
	def error(self, error:Exception):
		raise Exception("Unimplemented")