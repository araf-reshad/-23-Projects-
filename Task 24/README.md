## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #23 or are waiting for it to be marked.**

Choose between watching all the videos or reading all of the notes.

* Mouse Interaction in Pygame ([video](https://www.youtube.com/watch?v=u9gxpxMWva0&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.15%20Mouse%20Interaction%20in%20Pygame.md))
* Keyboard Interaction in Pygame (Part 1) ([video](https://www.youtube.com/watch?v=isPI9DkGdvQ&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note]([https://github.com/MissStrong/ICS3U/blob/main/Unit%203/8.2%20Keyboard%20Interaction%20in%20Pygame%20(Part%201).md](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.16%20Keyboard%20Interaction%20in%20Pygame%20(Part%201).md)))
* Keyboard Interaction in Pygame (Part 2) ([video](https://www.youtube.com/watch?v=hUJuj1iuvKI&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.17%20Keyboard%20Interaction%20in%20Pygame%20(Part%202).md))

## Instructions

Run the program to see what it does. Move your move around the screen and see what happens when you click the the screen.

Modify the program so that:
- the size of the square is always 100 by 100 
- left-clicking your mouse (single finger click) causes the square to change to a random colour
- right-clicking your mouse (double finger click) causes the background to change to a random colour
- the caption says "Random Colours"

## Criteria

* The program works exactly as decribed
* The initial comments are updated to describe your program

## main.py

Here is the original code in **main.py** for reference:

```python
# Initial setup
import pygame as pg
pg.init()
screen = pg.display.set_mode((400, 300))
pg.display.set_caption("Dynamic Square")

# Initializes some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Sets the size of the box to be 50x50
box_size = [50, 50]

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
      # Increases the box size if the mouse was left-clicked
      if left_clicked:
        box_size[0] += 10
        box_size[1] += 10
      # Decreases the box size if the mouse was right-clicked
      if right_clicked:
        box_size[0] -= 10
        box_size[1] -= 10

  # Paints the screen white
  screen.fill(WHITE)

  # Sets the center of the box to be where the mouse is
  box_position = (mouse_x - box_size[0]/2, mouse_y - box_size[1]/2)

  # Re-draws the box
  pg.draw.rect(screen, BLACK, (box_position, box_size))

  # Updates the screen
  pg.display.update()
```
