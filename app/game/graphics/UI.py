import pygame
import random

class UI:
    
    def __init__(self):
        self._font = pygame.font.SysFont(None, 32)
        self._surfaces = {}
        self._initiate_surfaces()
        self._res_type = None
        return
    
    def _initiate_surfaces(self):
        self._surfaces["sun"] = {"text": "Sun: {value}", "x": 8, "y": 8}
        self._surfaces["nut"] = {"text": "Nutrients: {value}", "x": 8, "y": 48}
        self._surfaces["wat"]  = {"text": "Water: {value}", "x": 8, "y": 88}


    def update_ui_surface(self, cursor, resources):
        sun = resources["Sun"]
        nut = resources["Nutrients"]
        wat = resources["Water"]
        self._surfaces["sun"]["surface"] = self._font.render(self._surfaces["sun"]["text"].format(value=sun), True, (0, 0, 0))
        self._surfaces["nut"]["surface"] = self._font.render(self._surfaces["nut"]["text"].format(value=nut), True, (0, 0, 0))
        self._surfaces["wat"]["surface"] = self._font.render(self._surfaces["wat"]["text"].format(value=wat), True, (0, 0, 0))

    def draw_ui(self, screen):
        screen.blits(((self._surfaces["sun"]["surface"], (self._surfaces["sun"]["x"], self._surfaces["sun"]["y"])), 
                     (self._surfaces["nut"]["surface"], (self._surfaces["nut"]["x"], self._surfaces["nut"]["y"])), 
                     (self._surfaces["wat"]["surface"], (self._surfaces["wat"]["x"], self._surfaces["wat"]["y"]))))
