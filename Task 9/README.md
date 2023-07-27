## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Project #1.** It's okay if you are waiting for it to be reviewed.

Choose between watching all the videos or reading all of the notes.

* Functions ([video](https://www.youtube.com/watch?v=MNoJv75pAx8&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.01%20Functions.md))
* Docstrings ([video](https://www.youtube.com/watch?v=MgLbOTLN4-M&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.02%20Docstrings.md))
* Functions in Math versus Functions in Computer Science ([video](https://www.youtube.com/watch?v=7qz2hsyv658&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.03%20Functions%20in%20Math%20versus%20Functions%20in%20Computer%20Science.md))

## Instructions

Complete the function `num_roots()` so that takes the coeffecients *a*, *b*, and *c* in a quadratic function in the form *y = ax<sup>2</sup> + bx + c* (where *a ≠ 0*) and returns the number of real roots.

To check whether your function works, click on the checkmark on the left-hand side then click on **▷ Run Tests**.

*Hint:* Recall what the [discriminant](https://en.wikipedia.org/wiki/Discriminant) of a quadratic is.

## Criteria
* The Unit Tests pass
* The function works exactly as described
* The docstring weren't be moved or removed
* Your function includes *at least one (1)* helpful line comment (the docstring doesn't count for this)

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
def num_roots(a, b, c):
	"""Returns the number of real roots in the quadratic relation y = ax^2 + bx + c."""
	# What goes here?
	pass # Delete this line when you're done

# You can modify these to test whether your function works
print(num_roots(1, 4, 4)) # should print 1
print(num_roots(2, 0, 1)) # should print 0
print(num_roots(-1, 2, 6)) # should print 2
```
