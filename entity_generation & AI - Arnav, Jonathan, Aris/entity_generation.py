import pygame
import sys

WINDOW_SIZE = (500,500)
FPS = 30

pygame.init()
display = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

running = True

class Cell:
    '''
    A class to create a single cell, used for larger entity systems and point counters
    '''
    def __init__(self, x, y, radius, color):
        '''
        Constructs attributes for cell creation
        '''
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    
    def draw(self):
        '''
        Method to draw cell in PyGame window
        '''
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

class Entity:
    '''
    A class to create an organic fluid entity comprising of smaller cells
    '''
    def __init__(self, x, y, cells):
        '''
        Constructs attributes for entity creation
        '''
        self.x = x
        self.y = y
        self.cells = cells
    
    def spawn(self):
        for cell in cells:
            cell.draw()

    #TODO: add goto method



while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    
    pygame.display.update()
    clock.tick(FPS)