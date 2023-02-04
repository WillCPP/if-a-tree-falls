import pygame
from game.Actor import Actor
from game.graphics.Background import Background

class Game:

    def __init__(self):
        self.bg = Background()
        return

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((1024, 480))
        sprites = pygame.sprite.Group()
        Actor(sprites)
        clock = pygame.time.Clock()
        dt = 0
        while True:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    return

            sprites.update(events, dt)
            
            #screen.fill((30, 30, 30))
            self.draw_background(screen)
            sprites.draw(screen)
            pygame.display.update()

            dt = clock.tick(60)

    def draw_background(self, screen):
        screen.blits(tuple(self.bg.bg_args))
        
