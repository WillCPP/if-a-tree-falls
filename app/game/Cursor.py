import pygame

class Cursor():
    def __init__(self):
        self.surface = pygame.image.load("resources/cursor_01.png")
        self.pos_x = 15*32
        self.pos_y = 5*32

    def move_left(self):
        if self.pos_x > 0:
            self.pos_x -= 32

    def move_right(self):
        if self.pos_x < 1023 - 32:
            self.pos_x += 32

    def move_up(self):
        if self.pos_y > 0:
            self.pos_y -= 32

    def move_down(self):
        if self.pos_y < 479 - 32:
            self.pos_y += 32

    def draw(self, screen):
        screen.blit(self.surface, (self.pos_x, self.pos_y))
