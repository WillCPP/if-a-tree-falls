
class Condition:
    id : int
    name : str
    desc: str
    modList = []

    def __init__(self,id, name, desc, modL):
        self.id = id
        self.name = name
        self.desc = desc
        self.modList = modL

    def __eq__(self, other):
        if self.id == other.id:
            return True
        return False

class Modifiers:
    resoureName : str
    def modFunction(self, x):
        return self.passFunc(x)

    def __init__(self, name, passFunc):
        self.resoureName = name
        self.passFunc = passFunc

conditionDict = {
    "Root" : Condition(0,"Root", "", [Modifiers("Sun", lambda a : a - 2), Modifiers("Water", lambda a : a - 1), Modifiers("Nutrients", lambda a : a - 1)]),
    "New Branch" : Condition(1,"New Branch", "", [Modifiers("Sun", lambda a : a + 20), Modifiers("Water", lambda a : a - 4), Modifiers("Nutrients", lambda a : a - 4)]),
    "Large Branch" : Condition(2,"Large", "", [Modifiers("All", lambda a : a*a )]),
    "Medium Branch" : Condition(3,"Medium", "", [Modifiers("All", lambda a : a * a)]),
    "Small" : Condition(4,"Small", "", [Modifiers("All", lambda a : a * 1)]),
    "Start" : Condition(5,"Start", "", [Modifiers("All", lambda a : a * 0), Modifiers("Sun", lambda a : a - 2), Modifiers("Water", lambda a : a - 2), Modifiers("Nutrients", lambda a : a - 2)]),
    "Dying" : Condition(6,"Dying", "", [Modifiers("All", lambda a : a * .25)]),
    "Dead" : Condition(7,"Dead", "", [Modifiers("All", lambda a : a * 0)])
}
