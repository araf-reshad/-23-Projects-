## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #9.** It's okay if you are waiting for it to be reviewed.

Choose between watching all the videos or reading all of the notes.

* Lists ([video](https://www.youtube.com/watch?v=MT3zzL6g9bM&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.04%20Lists.md))
* List Methods ([video](https://www.youtube.com/watch?v=e1RttRT1xXA&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.05%20List%20Methods.md))
* Cumulative Algorithms ([video](https://www.youtube.com/watch?v=BHw8I2WHA4Y&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.06%20Cumulative%20Algorithms.md))

## Instructions

Complete the function `positive_product()` in the file **main.py** so that it returns the product of all the positive numbers in `num_list` (a list of numbers). If the list is empty or it does not contain any positive numbers, it returns `1`.

To check whether your function works, click on the checkmark on the left-hand side then click on **▷ Run Tests**.

**Reminder**: Zero is neither positive nor negative.

**Hint**: Look up what the *multiplicative identity* is.

## Criteria
* The Unit Tests pass
* The function works exactly as described
* The docstring wasn't moved or removed
* No modules are imported.
* Your function includes *at least one (1)* helpful line comment (the docstring doesn't count for this)

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
def positive_product(num_list):
  """Returns the product of all the positive numbers in num_list."""
  # What goes here?
  pass # Delete this line when you're done

# You can modify these to test whether your function works
print(positive_product([])) # should print 1
print(positive_product([-3, -1, -0.5, 0])) # should print 1
print(positive_product([2])) # should print 2
print(positive_product([2, 6])) # should print 12
print(positive_product([2, 6, -9])) # should print 12
```
