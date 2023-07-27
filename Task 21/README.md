## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #20.** It's okay if you are waiting for it to be marked.

Choose between watching all the videos or reading all of the notes.

* Textboxes in Tkinter ([video](https://www.youtube.com/watch?v=1MnC3a1z3iM&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.08%20Textboxes%20in%20Tkinter.md))
* Checkboxes in Tkinter ([video](https://www.youtube.com/watch?v=K2dkRWVLtb8&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.09%20Checkboxes%20in%20Tkinter.md))
* Radio Buttons in Tkinter ([video](https://www.youtube.com/watch?v=qDasZue55bQ&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.10%20Radio%20Buttons%20in%20Tkinter.md))

## Instructions

Create a Tkinter program that replicates the window below.

![](https://raw.githubusercontent.com/MissStrong/ICS3U/main/Images/Dice_Roller.gif)

Here are some details:
* The number of possible sides on a standard die are 4 (tetrahedron), 6 (cube), 8 (octahedron), 12 (dodecahedron), and 20 (icosahedron)
* The default value for the number of sides is **6**
* The number of dice can be any integer from 1 to 3, but you don't have to check that the user actually enters a valid number
* The default value for the number of dice is **2**
* Clicking the **Roll dice** button similates a dice roll using the number and type of dice specified

* When **Show sum** is selected, the dice results are displayed as an equation (e.g. "You rolled 3 + 5 + 6 = 14")
* When **Show sum** is not selected, the results are displayed individually (e.g. "You rolled 3, 5, 6")

**Hint:** You can use `sum()` to get the sum of the numbers in a list.

## Criteria

* The app works exactly as described
* Each function contains a docstring that briefly describes what the function does
* Each function includes *at least one (1)* helpful line comment (the docstring doesn't count for this)

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
from tkinter import *
window = Tk()

# What goes here?

mainloop()
```
