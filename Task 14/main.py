from turtle import *
from turtle import _CFG

# Removing the scrollers
_CFG["canvwidth"] = 1 
_CFG["canvheight"] = 1


# Initial setup
title("Flag of Kuwait")

shape("turtle")

speed(2)


# The official dimensions of the flag of Kuwait is 2:1
WIDTH = 420 

HEIGHT = 210

setup(WIDTH, HEIGHT)


# The hexadecimal values for the colours of the flag of Kuwait. White is not included, since its the default colour of the canvas
green = "#007A3D"

red = "#CE1126"

black = "#000000"


# Go to the starting position
penup()

goto(-WIDTH/2, HEIGHT/3)


# Draw the black part on the left
begin_fill()

color(black)

pendown()

goto(-WIDTH, HEIGHT)

goto(-WIDTH, -HEIGHT)

goto(-WIDTH/2, -HEIGHT/3)

goto(-WIDTH/2, HEIGHT/3)

end_fill()


# Draw the green part on top
begin_fill()

color(green)

goto(WIDTH, HEIGHT/3)

goto(WIDTH, HEIGHT)

goto(-WIDTH, HEIGHT)

goto(-WIDTH/2, HEIGHT/3)

end_fill()


# Draw the red part on the bottom
begin_fill()

color(red)

goto(-WIDTH/2, -HEIGHT/3)

goto(WIDTH, -HEIGHT/3)

goto(WIDTH, -HEIGHT)

goto(-WIDTH, -HEIGHT)

goto(-WIDTH/2, -HEIGHT/3)

end_fill()

hideturtle()

done()
