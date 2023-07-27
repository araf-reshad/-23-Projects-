## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #14.** It's okay if you are waiting for it to be reviewed.

Choose between watching the video or reading the note.

* Multiple Turtles ([video](https://www.youtube.com/watch?v=Ui8ynU302Xc&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.16%20Multiple%20Turtles.md))

## Instructions

Create a Turtle program that replicates the window below.

![](https://raw.githubusercontent.com/MissStrong/ICS3U/main/Images/Turtle_Swap_2.gif)

Here are some details:
* There are four turtles with different randomly generated colours
* The turtles are initially positioned to form four corners of a square
* The turtles move clockwise along the square, leaving a trail
* When the turtles all reach a corner, they re-orient themselves to face the direction they're about to move in

*Hint 1:* To generate a random colour you can generate a random RGB value. If you do this, don't forget to call `colormode(255)` first.

*Hint 2:* To make it look like the turtles are moving at the same time, move each turtle a few pixels at a time.


## Criteria
* Your program runs the animation exactly as described
* The title of the window is updated 
* Your program includes *at least one (1)* helpful line comment (the ones that are in the initial program don't count)

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
# Importing the turtle module
from turtle import *
from turtle import _CFG  # this dictionary to be imported separately
import random

# Resizes the default canvas size to prevent scrollbars
_CFG["canvwidth"] = 1 
_CFG["canvheight"] = 1

# Creates a window with the size 400 by 400
setup(400, 400)
title("Turtle Swap")

# Keeps the program running after the drawing is complete
done()
```
