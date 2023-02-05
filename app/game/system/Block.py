from .Resource import *


class Block:

    def __init__(self, id, name, resourceList):
        self.id = id
        self.name = name
        self.resourceList = resourceList

    def __str__(self):
        return "Block id: "+ str(self.id) + " Name: " + self.name

# resourceDict = {
#
#      [Resource(0, "Sun", ),
#      Resource(1, "Water"),
#      Resource(2, "Nutrients")]
#   }

blockDict = {

    0 : Block (0, "Soil", [Resource(1,"Water", 5), Resource(2,"Nutrients", 5)]
    ),
    1 : Block (1, "Ground Water", [Resource(1,"Water", 15)]
    ),
    2 : Block (2, "Organic Material",[Resource(1,"Water", 3), Resource(2,"Nutrients", 15)]
    ),
    3 : Block (3, "Sand", [Resource(1,"Water", -1), Resource(2,"Nutrients", 2)]
    ),
    4 : Block (4, "Clay", [Resource(1,"Water", 5), Resource(2,"Nutrients", 5)]
    ),
    5 : Block (5, "Sky", [Resource(0,"Sun", 15)]
    )
}
