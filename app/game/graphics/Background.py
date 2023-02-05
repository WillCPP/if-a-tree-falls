import pygame
import random

class Background:
    
    def __init__(self):
        self.bg_array = []
        self.bg_args = []
        self._gen_bg()
        return

    def _gen_bg(self):
        block_sky = pygame.Surface((32, 32))
        block_sky.fill(pygame.Color("cadetblue2"))
        block_soil = pygame.image.load("resources/ground_materials/soil.png")
        #block_soil.fill(pygame.Color("brown1"))
        block_groundwater = pygame.image.load("resources/ground_materials/groundwater.png")
        #block_groundwater.fill(pygame.Color("blue4"))
        block_organic = pygame.image.load("resources/ground_materials/organicMatter.png")
        #block_organic.fill(pygame.Color("brown4"))
        block_sand = pygame.image.load("resources/ground_materials/sand.png")
        #block_sand.fill(pygame.Color("sandybrown"))
        block_clay = pygame.image.load("resources/ground_materials/clay.png")
        #block_clay.fill(pygame.Color("darkgrey"))
        
        block_array = [block_soil, block_groundwater, block_organic, block_sand, block_clay, block_sky]
        
        sky_array = [self._gen_row_sky() for x in range(5)]
        ground_array = [self._gen_row_ground() for x in range(10)]
        self.bg_array = sky_array + ground_array
        for i, x in enumerate(self.bg_array):
            for j, y in enumerate(x):
                self.bg_args.append((block_array[self.bg_array[i][j]], (j*32, i*32)))

    def _gen_row_sky(self):
        row = [5 for x in range(32)]
        return row

    def _gen_row_ground(self):
        w_array = [50, 10, 10, 15, 5]
        row = [random.choices(range(5), weights=w_array, k=1)[0] for x in range(32)]
        return row

    def draw_background(self, screen):
        screen.blits(tuple(self.bg_args))
