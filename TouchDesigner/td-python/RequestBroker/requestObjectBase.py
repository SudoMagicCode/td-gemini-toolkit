from typing import Dict, Any, Self
from abc import ABC, abstractmethod


class RequestObjectBase(ABC):
    def __init__(self, input: Any):
        self._inputData = input
        self._status: dict[str, Any] = {}
        self._completed = False
        self._result: bytes = b""
        self._path: str = ""
        self._header: dict[str, str] = {}
        self._method: str = "POST"
        self._on_done_cb: callable = None
        self._on_error_cb: callable = None

    @property
    def onDone(self) -> callable:
        return self._on_done_cb

    @onDone.setter
    def onDone(self, cb: callable):
        self._on_done_cb = cb

    @property
    def onError(self) -> callable:
        return self._on_error_cb

    @onError.setter
    def onError(self, cb: callable):
        self._on_error_cb = cb

    def _resolve(
        self,
        statusCode: Dict[str, Any],
        headerDict: Dict[str, str],
        data: bytes = None,
    ) -> Self:
        self._result = data
        self._status = statusCode
        self._headerDict = headerDict
        _resolve_result = self.resolve(self._result)
        if _resolve_result is None:
            self._completed = True
            if self._on_done_cb is not None:
                self._on_done_cb()
        return _resolve_result

    def _error(self, error: Exception):
        self._completed = True
        if self._on_done_cb is not None:
            self._on_done_cb()
        self.error(error)

    def url(self, base: str) -> str:
        return f"{base}/{self._path}"

    def method(self) -> str:
        return self._method

    def header(self) -> dict[str, str]:
        return self._header

    def isCompleted(self) -> bool:
        return self._completed

    def input(self) -> Any:
        return self._inputData

    def result(self) -> bytes:
        if not self._completed:
            raise Exception("Request is incomplete")
        return self._result

    def statusCode(self) -> int:
        if not self._completed:
            raise Exception("Request is incomplete")
        return self._status["code"]

    def statusMessage(self) -> str:
        if not self._completed:
            raise Exception("Request is incomplete")
        return self._status["message"]

    @abstractmethod
    def resolve(self, result: bytes) -> Self:
        raise Exception("Unimplemented")

    @abstractmethod
    def error(self, error: Exception):
        raise Exception("Unimplemented")
