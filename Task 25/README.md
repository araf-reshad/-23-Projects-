## Before Starting This Task

**It's recommended that you only begin this task if you have already finished all of Unit 3.**

Choose between watching all the videos or reading all of the notes.

* Reading Plaintext Files ([video](https://www.youtube.com/watch?v=psGifOWmK-k&list=PLVD25niNi0BnTo_MGI8NI6WvVIXcC9khH)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%204/4.01%20Reading%20Plaintext%20Files.md))
* Error Handling ([video](https://www.youtube.com/watch?v=KxYiZB2o1tY&list=PLVD25niNi0BnTo_MGI8NI6WvVIXcC9khH)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%204/4.02%20Error%20Handling.md))
  
## Instructions

Complete the three functions in **main.py** according to these specifictaions:

`character_count(filepath)` takes a filepath and returns the total number of characters (as in letters, numbers, symbols, etc. ) in the file. This includes any whitespace such as spaces and newlines. If the filepath does not exist, it returns `None`.

`word_count(filepath)` takes a filepath and returns the total number of tokens in the file. If the filepath does not exist, it returns `None`.

`line_count(filepath)` takes a filepath and returns the total number of lines in the file. This includes  blank lines. If the filepath does not exist, it returns `None`.

There are six files provided for testing. Their filepaths are `"shakespeare_plays/"` followed by the filename. Here is an example:

```python
print(line_count("shakespeare_plays/hamlet.txt"))  # should print 6038
```

**Reminder:** `return None` is equivalent to `return`.

## Criteria
* The Unit Tests pass
* The functions works exactly as described
* The docstrings weren't be moved or removed
* Each function includes *at least one (1)* helpful line comment (the docstring doesn't count for this)

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
def character_count(filepath):
  """Returns the number of characters in the Shakespeare play."""
  try:
    with open(filepath, "r+") as f:
      # What goes here?
      pass # Delete this line when you're done
  except FileNotFoundError:
    return

def word_count(filepath):
  """Returns the number of tokens in the Shakespeare play."""
  try:
    with open(filepath, "r+") as f:
      # What goes here?
      pass # Delete this line when you're done
  except FileNotFoundError:
    return

def line_count(filepath):
  """Returns the number of lines in the Shakespeare play."""
  try:
    with open(filepath, "r+") as f:
      # What goes here?
      pass # Delete this line when you're done
  except FileNotFoundError:
    return
```
