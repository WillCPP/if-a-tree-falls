import pygame
from game.graphics.Background import Background
from game.graphics.Foreground import Foreground
from game.Cursor import Cursor
from game.system.System import Tree
from game.graphics.UI import UI

class Game:

    def __init__(self):
        self.bg = Background()
        self.fg = Foreground()
        self.cursor = Cursor()
        self.tree = Tree(self.bg.bg_array)
        self.ui = None
        return

    def start(self):
        pygame.init()
        self.ui = UI()
        self.fg.load_images()
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
                    if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                        self.fg.addFGElement(self.tree.tryToAddRoot(int(self.cursor.pos_x / 32), int(self.cursor.pos_y / 32)))
            
            self.bg.draw_background(screen)
            self.fg.draw_foreground(screen)
            self.cursor.draw(screen)
            self.ui.update_ui_surface(self.cursor, self.tree.resourceStock)
            self.ui.draw_ui(screen)
            pygame.display.update()

            clock.tick(60)

