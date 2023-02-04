import pygame
from game.graphics.Background import Background
from game.Cursor import Cursor

class Game:

    def __init__(self):
        self.bg = Background()
        self.cursor = Cursor()
        return

    def start(self):
        pygame.init()
        pygame.key.set_repeat(250)
        screen = pygame.display.set_mode((1024, 480))
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    return
                if e.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP]:
                        self.cursor.move_up()
                    if keys[pygame.K_DOWN]:
                        self.cursor.move_down()
                    if keys[pygame.K_LEFT]:
                        self.cursor.move_left()
                    if keys[pygame.K_RIGHT]:
                        self.cursor.move_right()

            
            #screen.fill((30, 30, 30))
            self.draw_background(screen)
            self.cursor.draw(screen)
            pygame.display.update()

            clock.tick(60)

    def draw_background(self, screen):
        screen.blits(tuple(self.bg.bg_args))
        
