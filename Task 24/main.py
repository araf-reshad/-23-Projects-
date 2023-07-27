# Initial setup
import pygame as pg
import random
pg.init()
screen = pg.display.set_mode((400, 300))
pg.display.set_caption("Random Colours") #Change caption to "Random Colours" 

# Initializes some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Adjust the size of the box to be 100x100
box_size = [100, 100]

#Generate a random colour 
def random_colour():
  return(random.randint(0,255), random.randint(0,255), random.randint(0,255))

#Initialize the colour of the box to be black and background to be white 
box_colour = BLACK 
background_colour = WHITE

# Sets the mouse coordinates to be (0, 0) until the mouse moves
mouse_x = 0
mouse_y = 0

# Keeps the program running
while True:
  # Checks for mouse activity
  for event in pg.event.get():
    if event.type == pg.MOUSEMOTION:
      # Gets the coordinates of the mouse
      mouse_x = pg.mouse.get_pos()[0]
      mouse_y = pg.mouse.get_pos()[1]
    if event.type == pg.MOUSEBUTTONDOWN:
      # Checks whether the mouse was clicked
      left_clicked = pg.mouse.get_pressed()[0]
      right_clicked = pg.mouse.get_pressed()[2]
      
      #Change box colour on left click
      if left_clicked:
        box_colour = random_colour()
      #Change background colour on right click
      if right_clicked:
        background_colour = random_colour()
        
  # Fills screen with current background colour
  screen.fill(background_colour)

  # Sets the center of the box to be where the mouse is
  box_position = (mouse_x - box_size[0]/2, mouse_y - box_size[1]/2)

  # Re-draw the box with its current colour
  pg.draw.rect(screen, box_colour, (box_position, box_size))

  # Updates the screen
  pg.display.update()
  