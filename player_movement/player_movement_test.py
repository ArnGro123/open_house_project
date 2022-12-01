import pygame
import sys

pygame.init()
display = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

class Circle:
    def __init__(self, x, y, radius, color, x_speed, y_speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed

    def draw(self):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

    def move_right(self):
        self.x += self.x_speed

    def move_left(self):
        self.x -= self.x_speed

    def move_down(self):
        self.y += self.y_speed

    def move_up(self):
        self.y -= self.y_speed 

# cell_coords = [Circle(x, y, 20, "red", 3, 3) for y in range(200, 250, 10) for x in range(200, 250, 10)]
cell = Circle(200, 200, 20, "red", 3, 3)
mouse_circle = Circle(0, 0, 10, "blue", 3, 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display.fill("black")

    mouse_coords = pygame.mouse.get_pos()
    mouse_circle.x, mouse_circle.y = mouse_coords
    mouse_circle.draw()
    
    # for cell in cell_coords:
    cell.draw()

    if cell.x < mouse_circle.x:
        cell.move_right()
    else:
        cell.move_left()

    if cell.y < mouse_circle.y:
        cell.move_down()
    else:
        cell.move_up()

    x_distance = abs(cell.x-mouse_circle.x) 
    y_distance = abs(cell.y-mouse_circle.y)
    print(x_distance)

    if x_distance > 150:
        cell.x_speed = 3
    elif 50 < x_distance <= 150:
        cell.x_speed = 2
    elif 0 < x_distance <= 50:
        cell.x_speed = 0.5
    else:
        cell.x_speed = 0
    
    if y_distance > 500:
        cell.y_speed = 3
    elif 300 < y_distance <= 500:
        cell.y_speed = 2
    elif 0 < y_distance <= 300:
        cell.y_speed = 0.5
    else:
        cell.y_speed = 0


    pygame.display.update()
    clock.tick(30)