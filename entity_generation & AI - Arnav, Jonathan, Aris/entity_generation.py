import pygame
import sys
import random

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
    def __init__(self, x, y, radius, color, x_speed, y_speed):
        '''
        Constructs attributes for cell creation
        '''
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
    
    def draw(self):
        '''
        Method to draw cell in PyGame window
        '''
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

    
class Entity:
    '''
    A class to create an entity comprising of smaller cells
    '''
    def __init__(self, x, y, color):
        '''
        Constructs attributes for entity creation
        '''
        self.x = x
        self.y = y
        self.color = color
        self.cells = [Cell(self.x+5*i, self.y+5*j, 10, self.color, 0, 0) for j in range(3) for i in range(3)]
    
    def draw(self):
        '''
        Method drawing Cell objects of Entity, and moving based on Cell velocities
        '''
        for cell in self.cells:
            cell.draw()
            cell.x += cell.x_speed
            cell.y += cell.y_speed

    def goto(self, x, y):
        '''
        Method changing position of Entity
        '''


        #TODO: Fix goto method, and direction

        for cell in self.cells:

            x_distance = abs(cell.x-x)
            y_distance = abs(cell.y-y)

            if x_distance > 150:
                cell.x_speed = random.randrange(5, 12)
            elif 50 < x_distance <= 150:
                cell.x_speed = random.randrange(1, 5)
            elif 0 < x_distance <= 50:
                cell.x_speed = 0.5
            else:
                cell.x_speed = 0 
            
            if y_distance > 150:
                cell.y_speed = random.randrange(5, 12)
            elif 50 < y_distance <= 150:
                cell.y_speed = random.randrange(1, 5)
            elif 0 < y_distance <= 50:
                cell.y_speed = 0.5
            else:
                cell.y_speed = 0
                

    # def spawn(self):
    #     '''
    #     Method creating Cell objects in a list and drawing them 
    #     '''
        
    #     for cell in self.cells:
    #         cell.draw()
    #         cell.x += cell.x_speed
    #         cell.y += cell.y_speed
            

    # def goto(self, x, y):
        
    #     for cell in self.cells:
    #         if cell.x < x:
    #             cell.x_speed = 5
    #             print(cell.x_speed)
    #         else:
    #             cell.x_speed = -5

    #         if cell.y < y:
    #             cell.y_speed = 5
    #         else:
    #             cell.y_speed = -5

            # x_distance = abs(cell.x-x) 
            # y_distance = abs(cell.y-y)

            # if x_distance > 150:
            #     cell.x_speed = random.randrange(5, 12)
            # elif 50 < x_distance <= 150:
            #     cell.x_speed = random.randrange(1, 5)
            # elif 0 < x_distance <= 50:
            #     cell.x_speed = 0.5
            # else:
            #     cell.x_speed = 0 
            
            # if y_distance > 150:
            #     cell.y_speed = random.randrange(5, 12)
            # elif 50 < y_distance <= 150:
            #     cell.y_speed = random.randrange(1, 5)
            # elif 0 < y_distance <= 50:
            #     cell.y_speed = 0.5
            # else:
            #     cell.y_speed = 0


player = Entity(250, 250, "red")

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill("black")

    player.draw()
    player.goto(250, 250)

    pygame.display.update()
    clock.tick(FPS)