## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #26.** It's okay if you are waiting for it to be marked.

Choose between watching all the videos or reading all of the notes.

* Packing and Unpacking ([video](https://www.youtube.com/watch?v=xwMN_z_GeE0&list=PLVD25niNi0BnTo_MGI8NI6WvVIXcC9khH)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%204/4.05%20Packing%20and%20Unpacking.md))
* Unlimited Arguments ([video](https://www.youtube.com/watch?v=0RwM5iESMVE&list=PLVD25niNi0BnTo_MGI8NI6WvVIXcC9khH)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%204/4.06%20Unlimited%20Arguments.md))
* Raising Errors ([video](https://www.youtube.com/watch?v=OeJ8xdp6CpA&list=PLVD25niNi0BnTo_MGI8NI6WvVIXcC9khH)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%204/4.07%20Raising%20Errors.md))
* Multiple Exceptions and More ([note](https://www.w3schools.com/python/python_try_except.asp))

## Instructions

Complete the function `consecutive_ints()` so that it takes integers that can be arranged into a list of consecutive integers and returns them in a list in ascending order. If the integers cannot be arranged into a list of consecutive integers, it `raise`s a `ValueError` with the error message `"The inputs must be arrangeable in consecutive order."`. If the arguments are not integers, it `raise`s a `TypeError` with the error message `"The inputs must be  integers."`.

Examples:

```python
print(consecutive_ints(4, 2, 1, 3))  # prints [1, 2, 3, 4]
print(consecutive_ints(4, 2, 1, 7))  # raises a ValueError
print(consecutive_ints("4", "2", "1", "3"))  # doesn't run because of the error above, but if it did it would raise a TypeError
```

**Reminder:** Consecutive numbers are one apart. The integers 5, 7, and 6 can be arranged in consecutive order (5, 6, 7) but the integers 5, 7, and 4 cannot be arranged in consecutive order since 6 is missing.

**Hint:** We can use `sorted()` on a tuple to create a list with all the values in ascending order.

## Criteria
* The Unit Tests pass
* The function works exactly as described
* The docstring wasn't moved or removed
* Your function includes *at least one (1)* helpful line comment (the docstring doesn't count for this)
* You include at least 3 of your own tests that return a list
* You include at least 1 of your own tests that raises a `TypeError`
* You include at least 1 of your own tests that raises a `ValueError`

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
def consecutive_ints(*nums):
  """Takes any number of integer arguments and returns them in a sorted list if they can be arranged in a consecutive order.
  
  Otherwise raises a custom TypeError or ValueError.
  """
  # What goes here?
  pass # Delete this line when you're done

# Include at least three tests here that should return a list
print(consecutive_ints(4, 1, 3, 2))

try:
  # Include a test here that should raise a TypeError
	pass
except TypeError:
  print("This raises a TypeError.")
except:
  print("This raises the wrong error.")

try:
    # Include a test here that should raise a TypeError
    print(consecutive_ints("4", "2", "1", "3"))
except TypeError:
    print("This raises a TypeError.")
except:
    print("This raises the wrong error.")
