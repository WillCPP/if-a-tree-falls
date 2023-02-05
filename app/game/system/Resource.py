
class Resource:

    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.value = value

    def __eq__(self, other):
        self.id == other.id


resourceDict = {

     "Sun" :Resource(0, "Sun", 0),
     "Water" :Resource(1, "Water", 0),
     "Nutrients": Resource(2, "Nutrients", 0)
   }
