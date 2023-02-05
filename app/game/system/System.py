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

class Position():
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "X: " + str(self.x) + " Y: " + str(self.y)

    ##def __str__(self):
    ##    return "X: " + self.x + " Y: " + self.y

class Node():
    id: int
    nodeType: str
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
        return  self.nodeType +": Id: " + str(self.id) + " Position: " + str(self.position) + " Orenitation: " + self.orenitation

    def __init__(self, id, nodeType, position, block, parentId, parentPosition = Position(-1,-1)):
        self.id = id
        self.nodeType = nodeType
        self.position = position
        self.block = block
        self.parentId = parentId
        self.parentPosition = parentPosition
        if parentId == -1:
            self.orenitation = "straightNS"
        else:
            self.startOrenitation()
        print(self)

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

    def startOrenitation(self):
        divx = self.parentPosition.x - self.position.x
        divy = self.parentPosition.y - self.position.y
        print(divx)
        print(divy)
        if divx > 0:
            self.west = True
        if divx < 0:
            self.east = True
        if divy > 0:
            self.north = True
        if divy < 0:
            self.south = True
        self.orenitation = self.getOrenitation()

    def addChildOrenitation(self, child):
        divx = self.position.x - child.position.x
        divy = self.position.y - child.position.y
        if divx < 0:
            self.west = True
        if divx > 0:
            self.east = True
        if divy < 0:
            self.north = True
        if divy > 0:
            self.south = True
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
    maxGridSizeX = 31
    maxGridSizeY = 14
    #dict with id of resource as key
    resourceStock = {"Sun": 0, "Water": 0, "Nutrients": 0}
    BlockGrid = []

    def _gen_row(self, idRow):
        #row = [random.choice(range(5)) for x in range(32)]
        row = [{"BlockId" : id, "Block": blockDict[id], "NodeId": -1} for id in idRow]
        print(len(row))
        return row


    def __init__(self, groundArray):
        self.rootIdCounter = 0
        self.branchIdCounter = 0
        startingPoint = Position(15,5)
        startBranchPoint = Position(15,4)
        self.BlockGrid = [self._gen_row(row) for row in groundArray]
        print(len(self.BlockGrid))
        #self, id, type, position, block, parentId, parentPosition
        startRoot = Node(self.rootIdCounter, "Root", startingPoint, self.BlockGrid[startingPoint.y][startingPoint.x].get("Block"),-1, startingPoint)
        self.rootList.append(startRoot)
        self.rootIdCounter += 1
        startBranch = Node(self.branchIdCounter, "Branch", startBranchPoint, self.BlockGrid[startBranchPoint.y][startBranchPoint.x].get("Block"),-1, startBranchPoint)
        self.branchList.append(startBranch)
        self.branchIdCounter += 1

    def __repr__(self):
        return "Tree: Resource Stock: " #+ self.resourceStock

    def updateResources(self, flow, flowDirection):
        id = flow.resource.id
        currentStock = self.resourceStock.get(id)
        if flowDirection:
            self.resourceStock.update(id, currentStock + flow.rate)
        else:
            self.resourceStock.update(id, currentStock - flow.rate)

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
        self.updateRoots()
        self.updateBranch()

    def getParentRoot(self, parentId):
        for root in self.rootList:
            print ("THE ROOOTS: " + str(root.id))
            if root.id == parentId:
                return root
        return None
    #def updateParentOrenintation(self):

    def addRoot(self, position, parentId):
        parentRoot = self.getParentRoot(parentId)
        print(self.BlockGrid[position.y][position.x].get("Block"))
        print("Adding Root At " + str(position) + " ParentId: " + str(parentId))
        print(parentRoot)
        if  parentRoot is  None:
            newRoot = Node(self.rootIdCounter, "Root", position, self.BlockGrid[position.y][position.x].get("Block"),-1)

        else:
            newRoot = Node(self.rootIdCounter, "Root", position, self.BlockGrid[position.y][position.x].get("Block"),parentId, parentRoot.position)
            parentRoot.addChildOrenitation(newRoot)
        self.rootList.append(newRoot)
        self.BlockGrid[position.y][position.x]["NodeId"] = self.rootIdCounter

        self.rootIdCounter += 1

    def positionBlockInfo(self, x, y):
        return Block(self.BlockGrid[y][x].get("Block"))

    def rootOnBlock(self, x, y):
        if x < 0 or y < 0 or x > self.maxGridSizeX or y > self.maxGridSizeY:
            return -1
        nodeId = self.BlockGrid[y][x].get("NodeId")
        if  nodeId!= -1:
            return nodeId
        return -1

    def tryToAddRoot(self, x, y):
        if self.rootOnBlock(x , y) != -1:
            return
        northRoot = self.rootOnBlock(x ,y-1)
        westRoot =  self.rootOnBlock(x-1 , y)
        eastRoot = self.rootOnBlock(x+1 ,y)
        southRoot =  self.rootOnBlock(x , y-1)
        pos = Position(x,y)
        if northRoot != -1:
            self.addRoot(pos, northRoot)
        elif westRoot != -1:
            self.addRoot(pos, westRoot)
        elif eastRoot != -1:
            self.addRoot(pos, eastRoot)
        elif southRoot != -1:
            self.addRoot(pos, southRoot)




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
