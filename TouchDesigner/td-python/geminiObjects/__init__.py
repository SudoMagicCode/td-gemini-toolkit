from contents import *
from models import *
from operations import RpcOperations
from vars import *
from generationConfig import *

import operatorAdaptors

# adapts touchdesigner operators to gemini objects
Adaptors = operatorAdaptors

# gemini specific enums
Operation = RpcOperations
