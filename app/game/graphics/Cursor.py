import pygame
import random

class Cursor:

    def __init__(self):
        self.cursor_surface = self._set_surface()

    def _set_surface(self):
        return pygame.image.load("resources/cursor_01.png")

