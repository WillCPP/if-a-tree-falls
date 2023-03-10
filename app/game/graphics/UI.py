import pygame
import random

class UI:
    
    def __init__(self):
        self._font = pygame.font.SysFont(None, 32)
        self._font_end = pygame.font.SysFont(None, 128)
        self._surfaces = {}
        self._res_uis = []
        self._initiate_surfaces()
        return
    
    def _initiate_surfaces(self):
        self._surfaces["sun"] = {"text": "Sun: {value}", "x": 8, "y": 8}
        self._surfaces["nut"] = {"text": "Nutrients: {value}", "x": 8, "y": 48}
        self._surfaces["wat"] = {"text": "Water: {value}", "x": 8, "y": 88}
        self._surfaces["hel"] = {"text": "Health: {value}", "x": 8, "y": 128}
        s_t = pygame.Surface((0, 0))
        self._res_uis = [pygame.image.load("resources/ui/info_soil.png"), pygame.image.load("resources/ui/info_groundwater.png"), pygame.image.load("resources/ui/info_organic.png"), pygame.image.load("resources/ui/info_sand.png"), pygame.image.load("resources/ui/info_clay.png"), s_t]
        self._surfaces["info"] = {"x": 838, "y": 8}
        self._surfaces["info"]["surface"] = self._res_uis[5]
        self._surfaces["win"] = {"text": "You Win!", "x": 256, "y": 128}
        self._surfaces["lose"] = {"text": "You Lose.", "x": 256, "y": 128}
        self._surfaces["lose2"] = {"x": 0, "y": 0}
        self._surfaces["win"]["surface"] = self._font_end.render(self._surfaces["win"]["text"], True, (0, 0, 0))
        self._surfaces["lose"]["surface"] = self._font_end.render(self._surfaces["lose"]["text"], True, (0, 0, 0))
        self._surfaces["lose2"]["surface"] = pygame.image.load("resources/ui/you-lose.png")

    def update_ui_surface(self, id, resources, treehealth):
        sun = resources["Sun"]
        nut = resources["Nutrients"]
        wat = resources["Water"]
        hel = treehealth
        self._surfaces["sun"]["surface"] = self._font.render(self._surfaces["sun"]["text"].format(value=sun), True, (0, 0, 0))
        self._surfaces["nut"]["surface"] = self._font.render(self._surfaces["nut"]["text"].format(value=nut), True, (0, 0, 0))
        self._surfaces["wat"]["surface"] = self._font.render(self._surfaces["wat"]["text"].format(value=wat), True, (0, 0, 0))
        self._surfaces["hel"]["surface"] = self._font.render(self._surfaces["hel"]["text"].format(value=hel), True, (0, 0, 0))
        self._surfaces["info"]["surface"] = self._res_uis[id]

    def draw_ui(self, screen):
        screen.blits(((self._surfaces["sun"]["surface"], (self._surfaces["sun"]["x"], self._surfaces["sun"]["y"])), 
                     (self._surfaces["nut"]["surface"], (self._surfaces["nut"]["x"], self._surfaces["nut"]["y"])), 
                     (self._surfaces["wat"]["surface"], (self._surfaces["wat"]["x"], self._surfaces["wat"]["y"])),
                     (self._surfaces["hel"]["surface"], (self._surfaces["hel"]["x"], self._surfaces["hel"]["y"])),
                     (self._surfaces["info"]["surface"], (self._surfaces["info"]["x"], self._surfaces["info"]["y"]))))

    def draw_end_ui(self, screen, lose, win):
        if win and not lose:
            screen.blit(self._surfaces["win"]["surface"], (self._surfaces["win"]["x"], self._surfaces["win"]["y"]))
        if lose and not win:
            screen.blit(self._surfaces["lose2"]["surface"], (self._surfaces["lose2"]["x"], self._surfaces["lose2"]["y"]))

