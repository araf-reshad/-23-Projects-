# Importing the turtle module
from turtle import *
from turtle import _CFG  # this dictionary to be imported separately

# Resizes the default canvas size to prevent scrollbars
_CFG["canvwidth"] = 1 
_CFG["canvheight"] = 1

# Creates a window with the size 400 by 300
setup(400, 300)

#Title
title("Turtle Spirals")

name = input("Name your turtle: ") 

print("How fast is " + name + "?")

speed = int(input("Enter a number between 1 and 10: "))

print("What colour should " + name + " be?")

turtle_color = input("Enter a hexadecimal number beginning with '#': ")

print("What angle should " + name + " make the spiral?")

angle = int(input("Enter a number between 20 and 80: ")) #casts into int because angle must be integer

print("Click on " + name + " to begin.")

color(turtle_color)

shape("turtle")

showturtle()

def spiral(x,y): 
  forward_distance = 0
  
  while True: 
    forward(forward_distance)
    
    forward_distance+=1 #increases length of spiral by 1 each time the turtle moves
    
    left(angle)
    
onclick(spiral) #makes spiral when clicked

# Keeps the program running after the drawing is complete
done()