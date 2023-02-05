
class Condition:
    name : str
    desc: str
    modList = []

    def __init__(self, name, desc, modL):
        self.name = name
        self.desc = desc
        self.modList = modL

class Modifiers:
    resoureName : str
    def modFunction(self, x):
        return self.passFunc(x)

    def __init__(self, name, passFunc):
        self.resoureName = name
        self.passFunc = passFunc

conditionDict = {
    "Large" : Condition("Large", "", [Modifiers("All", lambda a : a * 4)]),
    "Medium" : Condition("Medium", "", [Modifiers("All", lambda a : a * 2)]),
    "Small" : Condition("Small", "", [Modifiers("All", lambda a : a * 1)]),
    "Start" : Condition("Start", "", [Modifiers("All", lambda a : a * 0), Modifiers("Sun", lambda a : a - 2), Modifiers("Water", lambda a : a - 2), Modifiers("Nutrients", lambda a : a - 2)]),
    "Dying" : Condition("Dying", "", [Modifiers("All", lambda a : a * .25)]),
    "Dead" : Condition("Dead", "", [Modifiers("All", lambda a : a * 0)])
}
