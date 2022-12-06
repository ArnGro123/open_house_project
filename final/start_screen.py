import pygame
import sys
import pygame_gui

WINDOW_SIZE = (500,500)
FPS = 30

pygame.init()
display = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

running = True

class StartScreen:
    '''
    A class to create the opening menu for the game
    '''
    def __init__(self, screen_length, screen_width):
        '''
        Constructs UI manager and elements
        '''
        self.screen_length = screen_length
        self.screen_width = screen_width
        self.manager = pygame_gui.UIManager((self.screen_length, self.screen_width))

        #TODO: Add Game Title
        #TODO: Add Player Entry Box
        #TODO: Add Run Button

    def process_events(self, event):
        '''
        Method to check event occurrence
        '''
        self.manager.process_events(event)

    def update(self, time_delta):
        '''
        Method to update time of UI Manager
        '''
        self.manager.update(time_delta)

    def draw_ui(self):
        '''
        Method to draw elements to screen
        '''
        self.manager.draw_ui(display)

start_screen = StartScreen(WINDOW_SIZE[0], WINDOW_SIZE[1])

while running == True:

    clock.tick(FPS)
    time_delta = clock.tick(FPS)/1000
    start_screen.update(time_delta)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        start_screen.process_events(event)

    display.fill("black")

    start_screen.draw_button()

    start_screen.draw_ui()
    pygame.display.update()