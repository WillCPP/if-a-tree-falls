import pygame
import random

class Background:
    
    def __init__(self):
        self._bg_array = []
        self.bg_args = []
        self._gen_bg()
        return

    def _gen_bg(self):
        block = pygame.Surface((32, 32))
        block.fill(pygame.Color("lightgoldenrod"))
        block2 = pygame.Surface((32, 32))
        block2.fill(pygame.Color("lightgray"))
        self._bg_array = [self._gen_row() for x in range(15)] 
        for i, x in enumerate(self._bg_array):
            for j, y in enumerate(x):
                self.bg_args.append((block if ((i+j)%2) == 0 else block2, (j*32, i*32)))

    def _gen_row(self):
        row = [random.choice(range(5)) for x in range(32)]
        return row
