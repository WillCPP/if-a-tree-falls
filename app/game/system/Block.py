from .Resource import Resource


class Block:

    def __init__(self, id, name, resourceList):
        self.id = id
        self.name = name
        self.resourceList = resourceList

    def __str__(self):
        return "Block id: "+ str(self.id) + " Name: " + self.name

resourceDict = {
    "Sun" : Resource(0, "Sun"),
    "Water" : Resource(1, "Water"),
    "Nutrients" : Resource(2, "Nutrients")
 }
blockDict = {

    0 : Block (0, "Soil", [{resourceDict["Water"]: 5}, {resourceDict["Nutrients"]: 5}]
    ),
    1 : Block (1, "Ground Water", [{resourceDict["Water"]: 15}]
    ),
    2 : Block (2, "Organic Material",[{resourceDict["Water"]: 3}, {resourceDict["Nutrients"]: 15}]
    ),
    3 : Block (3, "Sand", [{resourceDict["Water"]: -1}, {resourceDict["Nutrients"]: 1}]
    ),
    4 : Block (4, "Clay", [{resourceDict["Water"]: 5}, {resourceDict["Nutrients"]: 5}]
    ),
    5 : Block (5, "Sky", [{resourceDict["Sun"]: 15}]
    )
}
