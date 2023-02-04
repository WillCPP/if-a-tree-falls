import pygame
from game.Actor import Actor

#class Actor(pygame.sprite.Sprite):
#    def __init__(self, *args):
#        super().__init__(*args)
#        self.image = pygame.Surface((32, 32))
#        self.rect = pygame.display.get_surface().get_rect()
#        self.image.fill(pygame.Color('dodgerblue'))
#
#    def update(self, events, dt):
#        self.rect.move_ip((1 * dt / 5, 2 * dt / 5))
#        if self.rect.x > 500: self.rect.x = 0
#        if self.rect.y > 500: self.rect.y = 0

#def main():
#    pygame.init()
#    screen = pygame.display.set_mode((500, 500))
#    sprites = pygame.sprite.Group()
#    Actor(sprites)
#    clock = pygame.time.Clock()
#    dt = 0
#    while True:
#
#        events = pygame.event.get()
#        for e in events:
#            if e.type == pygame.QUIT:
#                return
#
#        sprites.update(events, dt)
#
#        screen.fill((30, 30, 30))
#        sprites.draw(screen)
#        pygame.display.update()
#
#        dt = clock.tick(60)

#if __name__ == '__main__':
#    main()


class Game():

    def __init__(self):
        return

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
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
            
            screen.fill((30, 30, 30))
            sprites.draw(screen)
            pygame.display.update()

            dt = clock.tick(60)
