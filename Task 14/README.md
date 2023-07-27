## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #13.** It's okay if you are waiting for it to be reviewed.

Choose between watching all the videos or reading all of the notes.

* Turtle Basics ([video](https://www.youtube.com/watch?v=lLGbfdw7lUk&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.12%20Turtle%20Basics.md))
* Movement in Turtle ([video](https://www.youtube.com/watch?v=mUVG0lZYx-4&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.13%20Movement%20in%20Turtle.md))
* Shapes Coordinates in Turtle ([video](https://www.youtube.com/watch?v=PDcMSORYDcM&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.14%20Shapes%20in%20Turtle.md))
* Colours in Turtle ([video](https://www.youtube.com/watch?v=N-DQgmRorxA&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.15%20Colours%20in%20Turtle.md))

## Instructions

Modify the given program so that it draws and displays the flag of one of these countries:

* Bahamas
* Jamaica
* Kuwait
* Seychelles
* Guyana

Search online to find or calculate:
* the flag's dimensions
* exact RGB or hexadecimal values of the colours on the flag
* exact coordinates of each of the individual shapes on the flag

As an example, the program provided in **main.py** draws the flag of Laos.

## Criteria
* Your program shows an animation of a flag of your choice from the 5 options
* The title of the window is updated 
* The flag's size, colours, and shapes are accurate
* The comments in the program are updated to describe the flag you chose

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
from turtle import *
from turtle import _CFG

# This is for removing the scrollers
_CFG["canvwidth"] = 1 
_CFG["canvheight"] = 1

# Initial setup
title("Flag of Laos")
shape("turtle")
speed(2)

# The dimensions of the flag have a ratio of 3:2
WIDTH = 450
HEIGHT = 300
setup(WIDTH, HEIGHT)

# The hexadecimal values for the three colours of the Laotian flag
blue = "#002868"
white = "#FFFFFF"
red = "#CE1126"

# Top Red
color(red)
penup()
goto(-WIDTH/2, HEIGHT/2)
pendown()
begin_fill()
forward(WIDTH)
right(90)
forward(HEIGHT/4)
right(90)
forward(WIDTH)
end_fill()

# Middle Blue
color(blue)
begin_fill()
backward(WIDTH)
left(90)
forward(HEIGHT/2)
right(90)
forward(WIDTH)
end_fill()

# Bottom Red
color(red)
begin_fill()
backward(WIDTH)
left(90)
forward(HEIGHT/4)
right(90)
forward(WIDTH)
end_fill()

# White Circle
color(white)
penup()
goto(0, -HEIGHT/5)
pendown()

begin_fill()
circle(-HEIGHT/5)
end_fill()

hideturtle()
done()
```
