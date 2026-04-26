import smOpUtils
from geminiTerminalLogs import msg_formatter


class EndpointGenerator:
    def __init__(self, ownerOp: OP) -> None:
        self.Owner = ownerOp
        self.WindowCOMP: windowCOMP = ownerOp.op("window1")
        self.default_preview_url: str = (
            "https://aiplatform.googleapis.com/v1/publishers/google"
        )
        msg_formatter("Endpoint Generator created")

    def Add(self) -> None:
        if self._validate_controls() == False:
            msg_formatter("WARNING - Endpoint missing required fields")
            return
        else:

            newApiEndpoint = smOpUtils.apiEndpoint(
                name=self.Owner.par.Endpointname.eval(),
                modelType=self.Owner.par.Endpointtype.eval(),
                baseUrl=self.Owner.par.Endpointbaseurl.eval(),
                previewUrl=self.Owner.par.Endpointpreviewurl.eval(),
                apiKey=self.Owner.par.Endpointapikey.eval(),
            )
            msg_formatter("Creating new API Endpoint", indent=1)
            smOpUtils.addEndpoint(
                name=newApiEndpoint.name,
                modelType=newApiEndpoint.modelType,
                baseUrl=newApiEndpoint.baseUrl,
                previewUrl=newApiEndpoint.previewUrl,
                apiKey=newApiEndpoint.apiKey,
            )
            self.Close()

    def Cancel(self) -> None:
        self.Close()

    def _validate_controls(self) -> bool:
        name = self.Owner.par.Endpointname.eval()
        endpointType = self.Owner.par.Endpointtype.menuIndex
        baseUrl = self.Owner.par.Endpointbaseurl.eval()
        previewUrl = self.Owner.par.Endpointpreviewurl.eval()
        apiKey = self.Owner.par.Endpointapikey.eval()

        inputPars = [name, endpointType, baseUrl, previewUrl, apiKey]
        if "" in inputPars:
            print(inputPars)
            return False
        else:
            return True

    def _clear_controls(self) -> None:
        self.Owner.par.Endpointname = ""
        self.Owner.par.Endpointtype.menuIndex = 0
        self.Owner.par.Endpointbaseurl = ""
        self.Owner.par.Endpointpreviewurl = self.default_preview_url
        self.Owner.par.Endpointapikey = ""

    def Open(self) -> None:
        self.Owner.par.Open = True
        self._clear_controls()
        self.WindowCOMP.par.winopen.pulse()
        self.Owner.setFocus()

    def Close(self) -> None:
        self.Owner.par.Open = False
        self.WindowCOMP.par.winclose.pulse()
