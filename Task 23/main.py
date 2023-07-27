# Initial setup
import pygame as pg

pg.init()
WIDTH = 400
HEIGHT = 300
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Coding Doge Meme")

# Initializing the colour of the text
BLACK = (0, 0, 0)

# Loads the meme image
doge_meme = pg.image.load("doge meme 2.jpg")

# Resizes the image to be 400x300 (the size of the screen)
doge_meme = pg.transform.scale(doge_meme, (WIDTH, HEIGHT))

# Puts the image onto the screen
screen.blit(doge_meme, (0, 0))

# Resizes the image to be icon-sized
success_kid = pg.transform.scale(doge_meme, (32, 24))

# Puts the image as the icon
pg.display.set_icon(doge_meme)

# Stores the Passion One font with font size 30
gold_font = pg.font.Font("Gold Drops.otf", 30)

# Stores the text with font styling
top_text1 = gold_font.render("Me When", True, BLACK)
top_text2 = gold_font.render("Replit Tasks", True, BLACK)
bottom_text = gold_font .render("Exist.", True, BLACK)

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
