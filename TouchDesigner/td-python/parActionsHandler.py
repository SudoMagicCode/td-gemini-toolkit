class ParActionsHandler:
    def __init__(self, ownerOp: OP,  actions: callable, debug: bool = False):
        self.OwnerOp = ownerOp
        self.actions = actions
        self.debug = debug

    def HandleParChange(self, par: Par):
        try:
            func = getattr(self.actions, par.name)
            func(par)
        except Exception as e:
            if self.debug:
                print(e)
            else:
                pass
        return
