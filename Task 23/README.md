## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #22 or are waiting for it to be marked.**

Choose between watching all the videos or reading all of the notes.

* Images in Pygame ([video](https://www.youtube.com/watch?v=tsQK786jbUg&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.13%20Images%20in%20Pygame.md))
* Text and Fonts in Pygame ([video](https://www.youtube.com/watch?v=amCoC07twSo&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.14%20Text%20and%20Fonts%20in%20Pygame.md))

## Instructions

Modify this program so that it displays a different meme with different text in a different font. Keep it PG.

When selecting a font, be sure to **download the TTF file legally** using sites like [Google Fonts](https://fonts.google.com/). The font that is commonly used for memes is called Impact™, but it's not always available under SysFont and it's trademarked so we shouldn't search online for its TTF file.

## Criteria
* The program has an image with overlaying text
* The image and text are PG
* The text is in a font different than the one provided
* The initial comments are updated to describe your program

## main.py

Here is the original code in **main.py** for reference:

```python
# Initial setup
import pygame as pg

pg.init()
WIDTH = 400
HEIGHT = 300
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Success Kid")

# Initializing the colour of the text
WHITE = (255, 255, 255)

# Loads the meme image
success_kid = pg.image.load("success_kid.jpg")

# Resizes the image to be 400x300 (the size of the screen)
success_kid = pg.transform.scale(success_kid, (WIDTH, HEIGHT))

# Puts the image onto the screen
screen.blit(success_kid, (0, 0))

# Resizes the image to be icon-sized
success_kid = pg.transform.scale(success_kid, (32, 24))

# Puts the image as the icon
pg.display.set_icon(success_kid)

# Stores the Passion One font with font size 30
passion_one_font = pg.font.Font("passion_one.ttf", 30)

# Stores the text with font styling
top_text1 = passion_one_font.render("Writes 200 lines of code", True, WHITE)
top_text2 = passion_one_font.render("without proofreading.", True, WHITE)
bottom_text = passion_one_font .render("It doesn\'t crash.", True, WHITE)

# Prepares the rectangle that the first line of the top text will appear on
top_rectangle1 = top_text1.get_rect()
top_rectangle1.centerx = WIDTH/2
top_rectangle1.top = 0

# Prepares the rectangle that the second line of the top text will appear on
top_rectangle2 = top_text2.get_rect()
top_rectangle2.centerx = WIDTH/2
top_rectangle2.top = top_rectangle1.height

# Prepares the rectangle that the bottom text will appear on
bottom_rectangle = bottom_text.get_rect()
bottom_rectangle.centerx = WIDTH/2
bottom_rectangle.bottom = HEIGHT

# Puts the text onto the screen
screen.blit(top_text1, top_rectangle1)
screen.blit(top_text2, top_rectangle2)
screen.blit(bottom_text, bottom_rectangle)

# Keeps the program running and updating
while True:
  pg.display.update()
```
