import pygame
import button

pygame.init()

#create game window
width = 800
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arial", 40)

#define colours
text_color = ("black")

#load button images
start_img = pygame.image.load("images/button_start.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()

#create button instances
resume_button = button.Button(0, -100, start_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill("red")

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Press 1 to start", font, text_color, 160, 250)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()