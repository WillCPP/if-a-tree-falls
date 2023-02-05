from .Requirement import *

class Health():
    maxHealth: int
    currentHealth: int
    requirementList = []
    #
    # def checkHealth(self):
    #     pass


class TreeHealth(Health):
    def __init__(self, max, health):
        self.maxHealth = max
        self.currentHealth = health
        self.requirementHealthy = requirementDict["Tree Healthy"]
        self.requirementStable = requirementDict["Tree Stable"]


    def updateHealth(self, resourceStock):
        if checkRequirements(self.requirementHealthy, resourceStock):
            print("Tree is Healthy")
            if self.currentHealth < self.maxHealth:
                self.currentHealth += 1
        elif checkRequirements(self.requirementStable, resourceStock):
            print("Tree is Stable")
        else:
            self.currentHealth -= 1
        return self.currentHealth
