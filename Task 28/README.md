## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #27.** It's okay if you are waiting for it to be marked.
Choose between watching all video or reading the note.

* Custom Keyword Arguments ([video](https://www.youtube.com/watch?v=VKBr9UIOUW0&list=PLVD25niNi0BnTo_MGI8NI6WvVIXcC9khH)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%204/4.08%20Custom%20Keyword%20Arguments.md))
* Dictionaries ([video](https://www.youtube.com/watch?v=TUBEgOklBJU&list=PLVD25niNi0BlwZxjcVF6-vcOdAicWlRjC)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%203/3.02%20Dictionaries.md))

## Instructions

Complete the function `merge_dictionaries()` in so that it takes an unlimited number of dictionaries, merges them, and returns the merged dictionary. If the same key appears in multiple dictionaries, the value in the *earliest* dictionary takes precedence. The function should also take an optional keyword argument `tiebreaker = "last"` that changes the behaviour so that if the same key appears in multiple dictionaries, the value in the *latest* dictionary takes precedence. If a keyword other than `tiebreaker` is used, the function will raise a `KeyError`. When the keyword `tiebreaker` is used but the argument is something other than `"first"` or `"last"`, it will raise a `ValueError`.

Here are some examples:

```python
d1 = {1: 2, 5: 10}
d2 = {5: 9}
print(merge_dictionaries(d1, d2)  # should print {1: 2, 5: 10}
print(merge_dictionaries(d1, d2, tiebreaker = "last"))  # should print {1: 2, 5: 9}
```

Include at least five of your own tests to show that you tested your function.

## Requirements to Pass

## Criteria
* The Unit Tests pass
* The function works exactly as described
* The docstring wasn't moved or removed
* Your function includes *at least one (1)* helpful line comment (the docstring doesn't count for this)
* You include at least 5 of your own tests

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
def merge_dictionaries(*dicts, **kwargs):
  """Merges multiple dictionaries together and returns it.
  When the same key appears in multiple dictionaries, 
  the value that appears in the earliest dictionary takes precedence, 
  unless the keyword argument `tiebreaker = "last"` is used, 
  in which case the value in the latest dictionary takes precedence.
  """
  # What goes here?
  pass # Delete this line when you're done

# Include at least five tests here.
print(merge_dictionaries({}))  # should print {}
```
