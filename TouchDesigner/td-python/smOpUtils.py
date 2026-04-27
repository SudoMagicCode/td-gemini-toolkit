from dataclasses import dataclass
import geminiTerminalLogs

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
GEMINI_PREVIEW_URL = "https://generativelanguage.googleapis.com/v1beta"


@dataclass
class geminiOP:
    name: str
    returnType: str
    studioEnumPar: str
    vertexEnumPar: str


@dataclass
class ModelAsPar:
    """"""

    model: enum
    label: str

    def __repr__(self) -> str:
        return self.label


@dataclass
class menuPars:
    """"""

    menuNames: list
    menuLabels: list

    @staticmethod
    def fromEnum(info: enum):
        menuNames = [each.name for each in info]
        menuLabels = [each.value for each in info]
        return menuPars(menuLabels=menuLabels, menuNames=menuNames)

    @staticmethod
    def fromEnumPar(info: enum):
        menuNames = [each.name for each in info]
        menuLabels = [each.value.label for each in info]
        return menuPars(menuLabels=menuLabels, menuNames=menuNames)


@dataclass
class apiEndpoint:
    """"""

    name: str
    modelType: str  # can be either `vertex` or `studio`
    baseUrl: str
    previewUrl: str
    apiKey: str

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def fromDict(cls, info: dict):
        return cls(
            name=info.get("name"),
            modelType=info.get("modelType"),
            baseUrl=info.get("baseUrl"),
            previewUrl=info.get("previewUrl"),
            apiKey=info.get("apiKey"),
        )

    def asDict(self) -> dict:
        info = {
            "name": self.name,
            "baseUrl": self.baseUrl,
            "previewUrl": self.previewUrl,
            "apiKey": self.apiKey,
            "modelType": self.modelType,
        }
        return info


# op used for capturing user's API key
api_pop_dialog = parent.geminiCOMP.op("base_assets/popDialog")


def find_gemini_ops() -> list[OP]:
    """Returns a list of all ops with the `gemini` tag"""
    gemini_ops = root.findChildren(tags=["gemini"])
    return gemini_ops


def find_gemini_ops_parent_exclusive() -> list[OP]:
    """Returns a list of all ops with the `gemini` tag, excluding the parent of the calling op"""
    gemini_ops = find_gemini_ops()
    return [each for each in gemini_ops if each.name != parent.geminiCOMP.name]


def get_api_key() -> None:
    """Opens a dialog for the user to enter their API key"""

    def pop_dialog_cb(info: dict) -> None:
        """Private callback for the pop dialog"""
        buttonIndex = info.get("buttonNum")
        api_key = info.get("enteredText")
        if buttonIndex == 1:
            createDefaultEndpoint(api_key)

        else:
            return None

    api_pop_dialog.Open(callback=pop_dialog_cb)


def createDefaultEndpoint(apiKey: str) -> None:
    # ensure we have endpoints to work with
    checkEndpoints()

    # fetch endpoints
    endpoints = parent.geminiCOMP.fetch("endpoints")

    # create new default
    newEndpoint = createEndpoint(
        "default", "studio", GEMINI_BASE_URL, GEMINI_PREVIEW_URL, apiKey=apiKey
    )
    endpoints["default"] = newEndpoint.asDict()
    updateApiEndpointPar()


def updateApiEndpointPar(targetOp: OP = parent.geminiCOMP) -> None:
    """"""
    endpoints = targetOp.fetch("endpoints", None)
    try:
        if endpoints == None:
            targetOp.par.Hasapikey = False
            clear_menu_par(targetOp, "Apiendpoint")
            return
        else:
            set_menu_par(targetOp, "Apiendpoint", targetOp.fetch("endpoints"))
    except Exception as e:
        geminiTerminalLogs.msg_formatter(e)


def addEndpoint(
    name: str, modelType: str, baseUrl: str, previewUrl: str, apiKey: str
) -> None:
    # ensure we have endpoints to work with
    checkEndpoints()
    endpoints = parent.geminiCOMP.fetch("endpoints")

    # create new endpoint
    newEndpoint = apiEndpoint(name, modelType, baseUrl, previewUrl, apiKey)

    # add to storage
    endpoints[newEndpoint.name] = newEndpoint.asDict()

    # update drop down pars
    updateApiEndpointPar()


def createEndpoint(
    name: str, modelType: str, baseUrl: str, previewUrl: str, apiKey: str
) -> apiEndpoint:
    return apiEndpoint(name, modelType, baseUrl, previewUrl, apiKey)


def checkEndpoints() -> None:
    """"""
    endpoints = parent.geminiCOMP.fetch("endpoints", None)
    if endpoints == None:
        geminiTerminalLogs.msg_formatter(
            f"{parent.geminiCOMP.name} creating endpoints dict"
        )
        endpoints = {}
        parent.geminiCOMP.store("endpoints", endpoints)


def set_par_state(targetOp: OP, par: str, state: bool) -> None:
    try:
        targetOp.par[par] = state
    except Exception as e:
        pass


def updateMenuSource(targetOp: OP, par: str, menuSource: str) -> None:
    try:
        targetOp.par[par].menuSource = menuSource

    except Exception as e:
        pass


def clear_menu_par(targetOp: OP, par: str):
    try:
        targetOp.par[par].menuNames = []
        targetOp.par[par].menuLabels = []
    except Exception as e:
        pass


def set_menu_par(targetOp: OP, par: str, endpoints: dict) -> None:
    try:
        targetOp.par[par].menuNames = list(endpoints.keys())
        targetOp.par[par].menuLabels = list(endpoints.keys())
    except Exception as e:
        pass
