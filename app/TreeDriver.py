
from game.system.System import *
from game.graphics.Background import Background



## sim the game loop and call loop
class TreeDriver:

    def __init__(self):
        self.bg = Background()
        self.tree = Tree(self.bg.bg_array)

    def start(self):
        self.tree.update()
