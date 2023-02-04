import pygame

class Actor(pygame.sprite.Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        #self.image = pygame.Surface((32, 32))
        self.image = pygame.image.load("resources/cursor_01.png")
        self.rect = pygame.display.get_surface().get_rect()
        #self.image.fill(pygame.Color('dodgerblue'))

    def update(self, events, dt):
        self.rect.move_ip((1 * dt / 5, 2 * dt / 5))
        if self.rect.x > 500: self.rect.x = 0
        if self.rect.y > 500: self.rect.y = 0
