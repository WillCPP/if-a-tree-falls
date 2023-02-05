from .Resource import *


class Requirement():
    name : str
    resourceList = []

    def __init__(self, name, resourceList):
        self.name = name
        self.resourceList = resourceList



requirementDict = {
    "Make Branch": Requirement("Make Branch", [Resource(1,"Water", 2), Resource(2,"Nutrients", 3)]),
    "New Branch": Requirement("New Branch", [Resource(1,"Water", 3), Resource(2,"Nutrients", 4)]),
    "New Root": Requirement("New Root", [Resource(0,"Sun", 1), Resource(2,"Nutrients", 1)]),
    "Medium Branch": Requirement("Medium Branch", [Resource(1,"Water", 5), Resource(2,"Nutrients", 5)]),
    "Large Branch": Requirement("Medium Branch", [Resource(1,"Water", 10), Resource(2,"Nutrients", 10)]),
    "Tree Healthy": Requirement("Tree Healthy", [Resource(0,"Sun", 5), Resource(1,"Water", 5), Resource(2,"Nutrients", 5)]),
    "Tree Stable": Requirement("Tree Stable", [Resource(1,"Water", 0), Resource(0,"Nutrients", 0)])
}

def checkRequirements(requirement, resourceStock):
    for resource in requirement.resourceList:
        if resourceStock[resource.name] < resource.value:
            print("Not enough " + resource.name + " to add/update " + requirement.name)
            return False
    return True
