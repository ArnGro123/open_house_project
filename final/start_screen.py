import pygame
import sys
import pygame_gui

pygame.init()
display = pygame.display.set_mode()
clock = pygame.time.Clock()

DISPLAY_SIZE = display.get_size()
FPS = 30
running = True

class StartScreen:
    '''
    A class to create the opening menu for the game
    '''
    def __init__(self, screen_length, screen_height):
        '''
        Constructs UI manager and elements
        '''
        self.screen_length = screen_length
        self.screen_height = screen_height
        self.manager = pygame_gui.UIManager((self.screen_length, self.screen_height))

        #TODO: Add Game Title --> bouncing image?

        #TODO: Add Player Entry Box --> store input in text file, on run

        self.text_box_length = self.screen_length / 3
        self.text_box_height = self.screen_height / 15
        self.text_box_x = (self.screen_length / 2) - (self.text_box_length / 2)
        self.text_box_y = (self.screen_height / 2) - (self.text_box_height / 2)
        self.text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(self.text_box_x, self.text_box_y, self.text_box_length, self.text_box_height), manager=self.manager,object_id='#main_text_entry')

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

start_screen = StartScreen(DISPLAY_SIZE[0], DISPLAY_SIZE[1])

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

    start_screen.draw_ui()
    pygame.display.update()