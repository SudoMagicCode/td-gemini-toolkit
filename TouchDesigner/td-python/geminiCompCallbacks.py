callbackText = """
def generateOffToOn():
	#print("generation starting")
	pass

def generateOnToOff():
	#print("generation complete")
	pass
"""


def Addcallbacks(par: Par) -> None:
    thisOp: OP = parent.geminiCOMP

    if thisOp.par.Callbacksdat == "":
        return
    else:
        callbacks_dat = thisOp.parent().create(textDAT, f"{thisOp.name}_callbacks")
        callbacks_dat.nodeX = thisOp.nodeX
        callbacks_dat.nodeY = thisOp.nodeY - 120
        callbacks_dat.dock = thisOp
        thisOp.par.Callbacksdat = callbacks_dat.name
        callbacks_dat.viewer = True
        callbacks_dat.text = callbackText
        callbacks_dat.par.language.menuIndex = 3
