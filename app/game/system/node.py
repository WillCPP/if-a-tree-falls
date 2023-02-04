from dataclasses import dataclass
import Collection

@dataclass
class Resource():
    id: int
    name: str
    maxFlow: float

class ResourceStock():
    id: int
    name: str
    amount: float

class Ground():
    resourceList = []

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
    outFlowList = []
    inFlowList = []
    ground: Ground
    minInFlow : Flow
    maxOutFlow: float
    id: int
    parentId: int
    position: Position
    parentPosition: Position
    north: Bool = False
    south: Bool = False
    east: Bool = False
    west: Bool = False
    orenitation: str

    def totalFlow():
        sum = 0
        for aFlow in outFlowList:
            sum += aFlow.rate
        return sum

    def canIncreaseResourceRate(resourceId):
        if (totalFlow() >= maxOutFlow):
            return false
        for flow in outFlowList:
            if (flow.resource.id == resourceId):
                if (flow.canIncreaseRate()):
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
            west = True
        if divx < 0:
            east = True
        if divy > 0:
            north = True
        if divy < 0:
            south = True
        orenitation = getOrenitation()

    def addChildOrenitation(child):
        ## switch statement to set orenitation

    def getOrenitation():
        if north and south and east and west:
            return = "quad"
        else if north and south and east:
            return = "tripleNSE"
        else if north and south and west:
            return = "tripleNSW"
        else if north and east and west:
            return = "tripleNWE"
        else if south and east and west:
            return = "tripleSWE"
        else if north and west:
            return = "cornerNW"
        else if north and east:
            return = "cornerNE"
        else if south and west:
            return = "cornerSW"
        else if south and east:
            return = "cornerSE"
        else if north and south:
            return = "straightNS"
        else if east and west:
            return = "straightWE"
        else if north:
            return = "endN"
        else if south:
            return = "endS"
        else if west:
            return = "endW"
        else if east:
            return = "endE"
        else:
            return = "empty"



class RootNodes(Node):


class BranchNodes(Node):

class Tree():
    rootList = []
    branchList = []

    #dict with id of resource as key
    resourceStock = {}

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

    def updateResources(flow, in):
        id = flow.resource.id
        currentStock = resourceStock.get(id)
        if in:
            resourceStock.update(id, currentStock + flow.rate)
        else:
            resourceStock.update(id, currentStock - flow.rate)

    def updateRoots():
        for rootList in root:
            for inFlow in root.inFlowList:
                updateResources(inFlow, True)
            for outFlow in root.outFlowList:
                updateResources(outFlow, False)

    def  updateBranch():
        for branch in branchList:
            for inFlow in branch.inFlowList:
                updateResources(inFlow, True)
            for outFlow in branch.outFlowList:
                updateResources(outFlow, False)

    def update():
        updateRoots()
        updateBranch()

    def getParentRoot(parentId):
        for root in rootList:
            if root.id == parentId:
                return root
        return null

    def updateParentOrenintation():


    def addRoot(position, parentId):
        parentRoot = getParentRoot(parentId)
