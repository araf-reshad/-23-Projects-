import pygame as pg
pg.init()

#Set dimensions of the window
WIDTH = 900
HEIGHT = 600

#Set Caption
pg.display.set_caption ("Flag of Republic of Congo")

#Create the screen
screen= pg.display.set_mode ((WIDTH, HEIGHT)) 

#Set the RGB values of the colours on the flag 
Green = (0,150,57)
Yellow = (255,209,0)
Red = (239,51,64)

#Fill the screen with yellow 
screen.fill (Yellow)

#Create green triangle on flag
points_green= ([(0,0), ((WIDTH*2)//3, 0),  (0,HEIGHT)])
pg.draw.polygon(screen, Green, points_green)

#Create red triangle on flag
points_red = [(WIDTH,0), (WIDTH//3, HEIGHT), (WIDTH, HEIGHT)]
pg.draw.polygon(screen, Red, points_red)

while True: 
  #Update the display
  pg.display.update()

  #Look for QUIT event
  for event in pg.event.get():
    if event.type == pg.QUIT: 
      pg.quit()
      quit()
  