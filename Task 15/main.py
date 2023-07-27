# Importing the turtle module
from turtle import *
from turtle import _CFG  
import random

# Resizes the default canvas size to prevent scrollbars
_CFG["canvwidth"] = 1 
_CFG["canvheight"] = 1

# Creates a window with the size 400 by 400
setup(400, 400)

# Title
title("Turtle Swap")

colormode(255)

# A list of 4 turtles 
turtleList = []
# The starting coordinates of the 4 turtles
starting_points = [(-100,100),  (-100, -100), (100,-100), (100,100)]

# Initializes the 4 turtles
# (Gives them their initial speed, colour, location, heading and speed)
for i in range(4): 
  turtleList.append(Turtle())
  
  turtleList[i].shape("turtle")
  
  turtleList[i].hideturtle()
  
  turtleList[i].penup()
  
  turtleList[i].goto(starting_points[i])
  
  turtleList[i].color(random.randint(0, 255), random.randint(0,255), random.randint(0,255))
  
  turtleList[i].setheading(90*i)
  
  turtleList[i].speed(1)
  
  turtleList[i].showturtle()
  
  turtleList[i].pendown()

# A variable to keep track of the number of pixels travelled by each turtle
distance_travelled = 0 

while True: 
  
  for i in range(4): 
    
    # If the turtle reaches the corner of the square, make it turn 
    if(distance_travelled==200):
      
      turtleList[i].right(90)
      
    turtleList[i].forward(5)

  distance_travelled%=200
  
  distance_travelled+=5
  
# # Keeps the program running after the drawing is complete
done()
