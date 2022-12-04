import pygame
import button

pygame.init()


width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Main Menu")
game_start = False
menu= "main"
font = pygame.font.SysFont("arialblack", 40)
text_color = ("black")


start_img = pygame.image.load("images/button_start.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()


start_button = button.Button(0, -100, start_img, 1)
options_button = button.Button(0, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

run = True
while run:

  screen.fill("red")


  if game_start == True:
   
    if menu == "main":
    
      if start_button.draw(screen):
        
        game_start = False
        
      if options_button.draw(screen):
        
        menu = "options"
        
      if quit_button.draw(screen):
        
        run = False
    
    if menu == "options":
   
      if back_button.draw(screen):
      
        menu = "main"
        
  else:
    
    draw_text("Press the ONE KEY to start", font, text_color, 160, 250)


  for event in pygame.event.get():
    
    if event.type == pygame.KEYDOWN:
      
      if event.key == pygame.K_1:
        
        game_start = True
        
    if event.type == pygame.QUIT:
      
      run = False

  pygame.display.update()

pygame.quit()
