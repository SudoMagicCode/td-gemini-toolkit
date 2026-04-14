from typing import Dict, Any, runtime_checkable
from abc import ABC, abstractmethod

from requestObjectBase import RequestObjectBase


class RequestBroker:
    """RequestBroker handles all requests to the API and brokers their responses through callbacks
    """

    def __init__(self, _thisOp: OP):
        self._thisOp = _thisOp
        self._apiKey = parent.geminiCOMP.fetch('gemini_apiKey')
        self._webclientDat: webclientDAT = self._thisOp.op("webclient1")
        self._requestLookup: Dict[int, RequestObjectBase] = {}
        pass

    def _makeRequest(self, requestObject: RequestObjectBase, url: str, method: str, header=None):
        '''internal request initializer, this method will create the request on the webclientDat'''
        id = self._webclientDat.request(
            url, method, header=header, data=requestObject.input())
        self._requestLookup[id] = requestObject
        pass

    def _completeRequest(self, statusCode: Dict[str, Any], headerDict: Dict[str, str], data: bytes, id: int):
        '''internal request completer, this method will resolve the RequestObjectBase with data from the webclientDat'''
        # find the request object
        requestObject = self._requestLookup[id]

        # check if an object was found
        if requestObject is None:
            del self._requestLookup[id]
            return

        try:
            # attempt to resolve the request object
            requestObject._resolve(statusCode, headerDict, data)
        except Exception as e:
            # something went wrong in the resolving code...
            print(e)

        # delete the request object from lookup
        del self._requestLookup[id]
        return

    def _completeRequestAsError(self, id: int, error: Exception):
        # find the request object
        requestObject = self._requestLookup[id]

        # check if an object was found
        if requestObject is None:
            del self._requestLookup[id]
            return

        try:
            # attempt to resolve the request object
            requestObject._error(error)
        except Exception as e:
            # something went wrong in the resolving code...
            print(e)

        # delete the request object from lookup
        del self._requestLookup[id]

    def MakeRequest(self, requestObject: RequestObjectBase):
        requestObject._header["x-goog-api-key"] = self._apiKey
        self._makeRequest(requestObject, url=requestObject.url(
        ), method=requestObject.method(), header=requestObject.header())
        pass

    def CompleteRequest(self, statusCode: Dict[str, Any], headerDict: Dict[str, str], data: bytes, id: int):
        self._completeRequest(statusCode, headerDict, data, id)
        pass

    def CompleteRequestAsError(self, id: int, error: Exception):
        self._completeRequestAsError(id, error)
        pass
