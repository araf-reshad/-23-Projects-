## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #17.** It's okay if you are waiting for it to be marked.

Choose between watching the video or reading the note.

* Dictionaries ([video](https://www.youtube.com/watch?v=TUBEgOklBJU&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note]([https://github.com/MissStrong/ICS3U/blob/main/Unit%203/2.1%20Dictionaries.md](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.02%20Dictionaries.md)))
  
## Instructions

Complete the function `list_counts()` in **main.py** so that it takes three lists of numbers and it returns a dictionary that shows how many lists each number appeared in.

Here is an example of what it should do:

```python
print(list_counts([10, 20, 30], [5, 10], [10, 30]))
# prints {10: 3, 20: 1, 30: 2, 5: 1} (it's okay if the order is different)
# explanation: 10 appeared in three lists, 20 appeared in one list, 30 appeared in two lists, 5 appeared in one list
```

## Criteria
* The Unit Tests pass
* The function works exactly as described
* The docstring wasn't moved or removed
* Your function includes *at least one (1)* helpful line comment (the docstring doesn't count for this)
* You include at least 3 of your own tests.

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
def list_counts(lst1, lst2, lst3):
  """Returns a dictionary in which:
  - the keys are all the items that appeared in the lists 
  - the values are the number of lists that the item appeared in
  """
  # What goes here?
  pass # Delete this line when you're done

# Include at least three other tests here
print(list_counts([], [], [])) # should print {}
```
