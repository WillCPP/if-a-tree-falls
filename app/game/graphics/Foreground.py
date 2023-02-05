import pygame
import random

class Foreground:
    
    def __init__(self):
        self.fg_array = []
        self.fg_args = []
        self._root_dict = {}
        return

    def load_images(self):
        self._root_dict["Root_E"] = pygame.image.load("resources/roots/Root_E.png")
        self._root_dict["Root_NE"] = pygame.image.load("resources/roots/Root_NE.png")
        self._root_dict["Root_N"] = pygame.image.load("resources/roots/Root_N.png")
        self._root_dict["Root_NSE"] = pygame.image.load("resources/roots/Root_NSE.png")
        self._root_dict["Root_NS"] = pygame.image.load("resources/roots/Root_NS.png")
        self._root_dict["Root_NSWE"] = pygame.image.load("resources/roots/Root_NSWE.png")
        self._root_dict["Root_NSW"] = pygame.image.load("resources/roots/Root_NSW.png")
        self._root_dict["Root_NW"] = pygame.image.load("resources/roots/Root_NW.png")
        self._root_dict["Root_SE"] = pygame.image.load("resources/roots/Root_SE.png")
        self._root_dict["Root_S"] = pygame.image.load("resources/roots/Root_S.png")
        self._root_dict["Root_SWE"] = pygame.image.load("resources/roots/Root_SWE.png")
        self._root_dict["Root_SW"] = pygame.image.load("resources/roots/Root_SW.png")
        self._root_dict["Root_WE"] = pygame.image.load("resources/roots/Root_WE.png")
        self._root_dict["Root_W"] = pygame.image.load("resources/roots/Root_W.png")

    def addFGElement(self, l):
        if l is None:
            return
        else:
            self.fg_array = self.fg_array + l

    def _build_args(self):
        self.fg_args = [(self._root_dict[b["file"]], (b["x"] * 32, b["y"] * 32)) for b in self.fg_array]
 
    def draw_foreground(self, screen):
        self._build_args()
        screen.blits(tuple(self.fg_args))
