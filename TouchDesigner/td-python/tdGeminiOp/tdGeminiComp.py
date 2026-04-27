from geminiTerminalLogs import msg_formatter
from tdGeminiObject import geminiOP
from geminiObjects import GeminiModel, StudioModels, VertexModels


class tdGeminiComp:
    """
    tdGeminiComp is a base class for all Gemini TD Components.
    """

    def __init__(self, ownerComp: OP, geminiOp: geminiOP = None):
        self.Owner = ownerComp
        self.geminiOp = geminiOp
        self.endpointTypeIsStudio = tdu.Dependency(True)
        self.Model = tdu.Dependency(
            GeminiModel(
                isPreview=False, modelLookup="models/gemini-3.1-flash-lite-preview"
            )
        )
        self.setup()
        msg_formatter(f"{self.Owner.name} Gemini COMP Init")

    def update_menu_source(self) -> None:
        if self.geminiOp != None:
            if self.Owner.par["Studiomodel"].isMenu:
                self.Owner.par["Studiomodel"].menuSource = self.geminiOp.studioEnumPar
                self.Owner.par["Vertexmodel"].menuSource = self.geminiOp.vertexEnumPar
            else:
                self.Owner.par["Studiomodel"] = self.geminiOp.vertexEnumPar
                self.Owner.par["Vertexmodel"] = self.geminiOp.studioEnumPar
            self.Owner.par["Opviewer"].menuSource = (
                'tdu.TableMenu(me.op("viewer_options"), nameCol=0, labelCol=1)'
            )

            self.Owner.par.opviewer.expr = "me.par.Opviewer"
            self.Owner.par.opviewer.readOnly = True
            self.Owner.par.Geminioptype.expr = "me.GeminiOp"
            self.Owner.par.Geminioptype.readOnly = True

    @property
    def EndpointTypeIsStudio(self) -> callable:
        return self.endpointTypeIsStudio

    @property
    def GeminiOp(self) -> geminiOP:
        return self.geminiOp

    def setGeminiModel(self) -> None:
        self.Model.val = GeminiModel()

    def setup(self):
        try:
            self.update_menu_source()
            self.UpdateEndpointType(self.ResolveEndpointInfo())
        except Exception as e:
            pass

    def UpdateEndpointType(self, storage_info: dict) -> None:
        modelType = storage_info.get("modelType", None)

        if modelType == None:
            # set to studio as default
            self.endpointTypeIsStudio.val = True

        else:
            # update based on key if it exists
            if modelType == "studio":
                self.endpointTypeIsStudio.val = True
            else:
                self.endpointTypeIsStudio.val = False

    def ResolveEndpointInfo(self) -> dict:
        """"""
        # skip - we are the API key server
        if parent.geminiCOMP.par.opshortcut.eval() == "geminiAPIKeyServer":
            pass
        else:
            # assign the owner op if no target op is provided
            endpoint_key = self.Owner.par.Apiendpoint.eval()

            endPoint_info = self.Owner.fetch("endpoints", {})
            storage_info = endPoint_info.get(endpoint_key, {})

            if storage_info == None:
                return None
            else:
                return storage_info

    def ResolveModel(self) -> GeminiModel:
        isStudio = self.EndpointTypeIsStudio.val

        if isStudio:
            current_model: GeminiModel = StudioModels[self.Owner.par.Studiomodel.eval()]

        else:
            current_model: GeminiModel = VertexModels[self.Owner.par.Vertexmodel.eval()]

        return current_model.value
