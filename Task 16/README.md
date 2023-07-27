## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #15.** It's okay if you are waiting for it to be reviewed.

Choose between watching the video or reading the note.

* Mouse Interaction in Turtle ([video](https://www.youtube.com/watch?v=h_WifRpnS3M&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.17%20Mouse%20Interaction%20in%20Turtle.md))

## Instructions

Create a Turtle program that gets user input and uses it to make a turtle travel in a spiral.

![](Turtle_Spirals_2.gif)

Here are the prompt questions:

* Name your turtle:
* How fast is {turtle_name}? Enter a number between 1 and 10: 
* What colour should {turtle_name} be? Enter a hexadecimal number beginning with '#':
* What angle should {turtle_name} make the spiral? Enter a number between 20 and 80:
* Click on {turtle_name} to begin.

You can assume that the user will enter valid inputs.

Here is the pseudocode for the spiral. The tickmarks (`) indicate variables that will be in your code.

```
set `angle` to some value between 20 and 80
set `length` to 0

repeat forever:
  make the turtle go forward `length` pixels
  increase `length` by 1
  make the turtle go left by `angle`
```

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

# Resizes the default canvas size to prevent scrollbars
_CFG["canvwidth"] = 1 
_CFG["canvheight"] = 1

# Creates a window with the size 400 by 300
setup(400, 300)

# What goes here?

# Keeps the program running after the drawing is complete
done()
```
