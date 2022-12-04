import pygame
import pygame_gui
import sys

pygame.init()

width, height = 1000, 500
SCREEN = pygame.display.set_mode((width, height))

pygame.display.set_caption("Comp Sci Club Input Screen")
arnav = pygame_gui.UIManager((1600, 900))
text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((50, 50), (200, 50)), manager=arnav,object_id='#main_text_entry')
clock = pygame.time.Clock()

def show_user_name(user_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Changes screens
        SCREEN.fill("#00f5ff")

        new_text = pygame.font.SysFont("Times New Roman", 50).render(f"Computer Science Club:  {user_name}", True, "white")
        text = new_text.get_rect(center=(width/2, height/2))
        SCREEN.blit(new_text, text)
        clock.tick(60)
        pygame.display.update()

def get_user_name():
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#main_text_entry'):
                show_user_name(event.text)
            
            arnav.process_events(event)
        
        arnav.update(UI_REFRESH_RATE)
        arnav.draw_ui(SCREEN)
        pygame.display.update()
    

get_user_name()