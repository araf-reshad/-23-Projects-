## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #5.** It's okay if you are waiting for it to be reviewed.

Choose between watching all the videos or reading all of the notes.

* [For Loops](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.24%20For%20Loops.md) 
* [The `range()` Function](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.25%20The%20range()%20Function.md) 
* [The `print()` Function](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.26%20The%20print()%20Function.md)

## Instructions

Create a program that prompts the user for a positive integer then prints a right-aligned pyramid using that number using the structure below

Here are some examples:

```
> Enter an integer between 1 and 5: 2
  1
2 3
> Enter an integer between 1 and 5: 5
        1
      2 3
    3 4 5
  4 5 6 7
5 6 7 8 9
> Enter an integer between 1 and 5: -3.4
That's not an integer between 1 and 5.

```
If the input is not an integer between f1 and 5, nothing happens (there should not be any red error message).

**Note:** The `[ ]*` in the test cases is something called a *regular expression*. This particular regular expression means that you can have any number of trailing whitespace at the end of the line – it does *not* mean you should print these symbols at the end of each line.

**Hint 1:** A nested loop is one of the simplest approaches for this kind of problem. Start by figuring out the outer loop (the leading whitespace and the first number in each row), then figure out the inner loop (the rest of the numbers in each row).

**Hint 2:** Consider finding an expression for the number of digits in each row and another expression for the number of leading spaces in each row.

## Criteria
* The Input/Output Tests pass
* Your program uses a loop to print the pyramids
* Your program includes *at least one (1)* helpful line comment

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference:

```python
height = input("Enter an integer between 1 and 5: ")

# Continue this program so that it responds to each input as described in the instructions
```
