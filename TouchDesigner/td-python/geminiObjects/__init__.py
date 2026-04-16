from contents import *
from models import Models
from operations import RpcOperations
from vars import *
from generationConfig import *

import operatorAdaptors

# adapts touchdesigner operators to gemini objects
Adaptors = operatorAdaptors

# gemini specific enums
Model = Models
Operation = RpcOperations
