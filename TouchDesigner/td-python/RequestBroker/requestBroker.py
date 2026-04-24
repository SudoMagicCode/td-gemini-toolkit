from typing import Dict, Any, runtime_checkable
from abc import ABC, abstractmethod
import uuid

from requestObjectBase import RequestObjectBase
from geminiTerminalLogs import msg_formatter


class CanceledRequestException(Exception):
    pass


class RequestBroker:
    """RequestBroker handles all requests to the API and brokers their responses through callbacks"""

    def __init__(self, _thisOp: OP):
        self.my_id = uuid.uuid5(uuid.NAMESPACE_OID, _thisOp.path)
        self._thisOp = _thisOp
        msg_formatter(
            f"initializing request broker {str(self.my_id)} at {self._thisOp.path}"
        )
        self._webclientDat: webclientDAT = self._thisOp.op("webclient1")
        self._requestLookup: Dict[int, RequestObjectBase] = {}
        pass

    @property
    def _apiKey(self) -> str:
        if parent.geminiCOMP.fetch("gemini_apiKey", None) == None:
            msg_formatter(
                "Missing api key, please ensure you've added an API key to your component"
            )
            self._thisOp.parent().addScriptError("Missing Gemini API Key")
            raise ValueError("Missing api key")
        else:
            return parent.geminiCOMP.fetch("gemini_apiKey")

    def _makeRequest(
        self,
        requestObject: RequestObjectBase,
        url: str,
        method: str,
        header=None,
    ) -> int:
        """internal request initializer, this method will create the request on the webclientDat"""
        id = self._webclientDat.request(
            url,
            method,
            header=header,
            data=requestObject.input(),
        )
        print(url)
        self._requestLookup[id] = requestObject
        msg_formatter(f"{self._thisOp.path} broker making request")
        return id

    def _completeRequest(
        self,
        statusCode: Dict[str, Any],
        headerDict: Dict[str, str],
        data: bytes,
        id: int,
    ):
        """internal request completer, this method will resolve the RequestObjectBase with data from the webclientDat"""

        # find the request object
        if id not in self._requestLookup:
            # there has been some issue with the request map resetting
            msg_formatter(
                f"request {id} not found in broker {str(self.my_id)} at {self._thisOp.path}"
            )
            pass

        requestObject = self._requestLookup[id]

        # check if an object was found
        if requestObject is None:
            del self._requestLookup[id]
            return

        try:
            # attempt to resolve the request object
            nextRequest = requestObject._resolve(
                statusCode,
                headerDict,
                data,
            )
            if nextRequest is not None:
                # run the next request in series
                run(
                    "args[0](args[1])",
                    self.MakeRequest,
                    nextRequest,
                    delayMilliSeconds=1000 * 3,
                )
        except Exception as e:
            # something went wrong in the resolving code...
            msg_formatter(
                f"{str(self.my_id)} at {self._thisOp.path} raised Exception for request {id}:{e}"
            )

        # delete the request object from lookup
        del self._requestLookup[id]
        return

    def _completeRequestAsError(self, id: int, error: Exception):

        # find the request object
        if id not in self._requestLookup:
            # there has been some issue with the request map resetting
            msg_formatter(
                f"request {id} not found in broker {str(self.my_id)} at {self._thisOp.path}"
            )
            pass

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
            msg_formatter(
                f"{str(self.my_id)} at {self._thisOp.path} raised Exception for request {id}:{e}"
            )

        # delete the request object from lookup
        del self._requestLookup[id]

    def _cancelRequest(self, id: int):
        self._webclientDat.closeConnection(id)

        # find the request object
        if id not in self._requestLookup:
            # there has been some issue with the request map resetting
            msg_formatter(
                f"request {id} not found in broker {str(self.my_id)} at {self._thisOp.path}"
            )
            pass

        requestObject = self._requestLookup[id]

        try:
            # attempt to resolve the request object
            requestObject._error(CanceledRequestException())

        except Exception as e:
            # something went wrong in the resolving code...
            msg_formatter(
                f"{str(self.my_id)} at {self._thisOp.path} raised Exception for request {id}:{e}"
            )

        # delete the request object from lookup
        del self._requestLookup[id]

    def MakeRequest(
        self, requestObject: RequestObjectBase, isPreview: bool = False
    ) -> int:

        endpointData = parent.geminiCOMP.mod.apiKeyActions.resolveEndpointInfo()
        base_url = endpointData["baseUrl"]
        key = endpointData["apiKey"]

        requestObject._header["x-goog-api-key"] = key

        if isPreview:
            base_url = endpointData["previewUrl"]

        id = self._makeRequest(
            requestObject,
            url=requestObject.url(base_url),
            method=requestObject.method(),
            header=requestObject.header(),
        )
        return id

    def CompleteRequest(
        self,
        statusCode: Dict[str, Any],
        headerDict: Dict[str, str],
        data: bytes,
        id: int,
    ):
        self._completeRequest(statusCode, headerDict, data, id)
        pass

    def CompleteRequestAsError(self, id: int, error: Exception):
        self._completeRequestAsError(id, error)
        pass

    def CancelRequest(self, id: int) -> None:
        self._cancelRequest(id)
