from dataclasses import dataclass
from .Block import *
from .Resource import *

class ResourceStock():
    id: int
    name: str
    amount: float

class Flow():
    resource: Resource
    rate: float

    def canIncreaseRate():
        if (rate < resource.maxFlow):
            return true
        return false
    def canDecreaseRate():
        if (rate > 0):
            return true
        return false
    def setRate(x):
        rate = x

@dataclass
class Position():
    x: int
    y: int

class Node():
    id: int
    type: str
    position: Position
    block: Block
    outFlowList = []
    inFlowList = []
    minInFlow : Flow
    maxOutFlow: float
    orenitation: str
    parentId: int
    parentPosition: Position

    north = False
    south = False
    east = False
    west = False

    def __repr__(self):
        return

    def __init__(self, id, type, position, block, parentId, parentPosition):
        self.id = id
        self.type = type
        self.position = poistion
        self.block = block
        self.parentId = parentId
        self.parentPosition = parentPosition

    def totalFlow(self):
        sum = 0
        for aFlow in outFlowList:
            sum += aFlow.rate
        return sum

    def canIncreaseResourceRate(resourceId):
        if (totalFlow() >= maxOutFlow):
            return false
        for flow in outFlowList:
            if (flow.resource.id == resourceId):
                #if (flow.canIncreaseRate()):
                return true
        return false

    def canDecreaseResourceRate(resourceId):
        for flow in outFlowList:
            if (flow.resource.id == resourceId):
                if (flow.canDecreaseRate()):
                    return true
        return false

    def startOrenitation():
        divx = parentPosition.x - position.x
        divy = parentPosition.y - poisition.y
        if divx > 0:
            self.west = True
        if divx < 0:
            self.east = True
        if divy > 0:
            self.north = True
        if divy < 0:
            self.south = True
        orenitation = getOrenitation()

    #def addChildOrenitation(child):

        ## switch statement to set orenitation

    def getOrenitation(self):
        north = self.north
        south = self.south
        west = self.west
        east = self.east
        if north and south and east and west:
            return "quad"
        elif north and south and east:
            return "tripleNSE"
        elif north and south and west:
            return "tripleNSW"
        elif north and east and west:
            return  "tripleNWE"
        elif south and east and west:
            return "tripleSWE"
        elif north and west:
            return "cornerNW"
        elif north and east:
            return "cornerNE"
        elif south and west:
            return "cornerSW"
        elif south and east:
            return  "cornerSE"
        elif north and south:
            return "straightNS"
        elif east and west:
            return "straightWE"
        elif north:
            return "endN"
        elif south:
            return "endS"
        elif west:
            return "endW"
        elif east:
            return "endE"
        else:
            return "empty"





#class BranchNodes(Node):

#class BlockGrid(groundArray):


class Tree:
    rootList = []
    branchList = []

    #dict with id of resource as key
    resourceStock = {}
    BlockGrid = []

    def _gen_row(self, idRow):
        #row = [random.choice(range(5)) for x in range(32)]
        row = [{id : blockDict[id]} for id in idRow]
        return row

    def __init__(self, groundArray):
        self.BlockGrid = [self._gen_row(row) for row in groundArray]


    def __repr__(self):
        return "Tree: Resource Stock: " + resourceStock + "\nRoot List: " + rootList + "\nBranch List: " + branchList



    def updateResources(self, flow, flowDirection):
        id = flow.resource.id
        currentStock = resourceStock.get(id)
        if flowDirection:
            resourceStock.update(id, currentStock + flow.rate)
        else:
            resourceStock.update(id, currentStock - flow.rate)

    def updateRoots(self):
        for root in self.rootList:
            for inFlow in root.inFlowList:
                updateResources(inFlow, True)
            for outFlow in root.outFlowList:
                updateResources(outFlow, False)

    def  updateBranch(self):
        for branch in self.branchList:
            for inFlow in branch.inFlowList:
                updateResources(inFlow, True)
            for outFlow in branch.outFlowList:
                updateResources(outFlow, False)

    def update(self):
        print(self)
        self.updateRoots()
        self.updateBranch()
        print(self)

    def getParentRoot(self, parentId):
        for root in rootList:
            if root.id == parentId:
                return root
        return null

    #def updateParentOrenintation(self):


    def addRoot(self, position, parentId):
        parentRoot = getParentRoot(parentId)

        #
        # def branchFlowIn(resourceId):
        #     sum = 0
        #     for branch in branchlist:
        #         sum += branch.getInResource(resourceId)
        #     return sum
        #
        # def branchFlowOut(resourceId):
        #     sum = 0
        #     for branch in branchlist:
        #         sum += branch.getOutResource(resourceId)
        #     return sum
        #
        # def rootFlowIn():
        #     for root in rootList:
        #         for flow in root.inFlowList:
        #             id = flow.resource.id
        #             resourceStock[id] = resourceStock[id] + flow.rate
        #
        # def rootFlowOut(resourceId):
        #     sum = 0
        #     for root in rootlist:
        #         sum += root.getOutResource(resourceId)
        #     return sum
