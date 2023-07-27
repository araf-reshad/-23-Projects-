## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #10.** It's okay if you are waiting for it to be reviewed.

Choose between watching all the videos or reading all of the notes.

* The `round()` Function ([video](https://www.youtube.com/watch?v=vuTCz1Gz7tc&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.07%20The%20round()%20Function.md))
* The `type()` Function ([video](https://www.youtube.com/watch?v=LwTJ8HRtVOA&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.08%20The%20type()%20Function.md))

## Instructions

Complete the function `round_numbers()` in the file **main.py** so that it takes a list of values of various data types and returns the same list except all numbers are rounded to the nearest multiple of 10 and all the non-numeric values are removed. If a number ends in 5, it will round up for positive numbers and round down for negative numbers.

To check whether your function works, click on the checkmark on the left-hand side then click on **▷ Run Tests**.

**Hint**: We cannot always modify a list as we are looping through it. Consider creating a new list or making a copy of the original list.

**Reminder**: The `round()` function uses [banker's rounding](https://rounding.to/understanding-the-bankers-rounding/), which rounds to the nearest even number for numbers that end in .5. However, we want numbers to round up for positive numbers and round down for negative numbers.

## Criteria
* The Unit Tests pass
* The function works exactly as described
* The docstring wasn't moved or removed
* Your function includes *at least one (1)* helpful line comment (the docstring doesn't count for this)

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
def round_numbers(mixed_list):
    """Returns a new list with all numbers from mixed_list rounded to the nearest 10 and all non-numeric values removed."""
  # What goes here?
  pass # Delete this line when you're done

# You can modify these to test whether your function works
print(round_numbers([])) # should print []
print(round_numbers(["hi", True ,"koala"])) # should print []
print(round_numbers([1])) # should print [0]
print(round_numbers([-15, "x", False])) # should print [-20]
print(round_numbers([-0.1, 0, 1.8, "abc", 13.6])) # should print [0.0, 0, 0.0, 10.0]
print(round_numbers([1, 11, 15, 21, 40, 99])) # should print [0, 10, 20, 20, 40, 100]
print(round_numbers([-25, -15.0, -5, 0, 5.0, 15])) # should print [-30, -20.0, -10, 0, 10.0, 20]
```
