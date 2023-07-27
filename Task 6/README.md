## Before Starting This Task

It's recommended that you **only begin this task if you have already submitted Task #5.** It's okay if you are waiting for it to be marked.

Choose between watching all the videos or reading all of the notes.

* [String Indexing](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.20%20String%20Indexing.md) 
* [Substrings and String Slicing](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.21%20Substrings%20and%20String%20Slicing.md)
* [Built-In String Methods](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.22%20String%20Methods.md)
* [Debugging](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.23%20Debugging.md)

## Instructions

The following program prompts the user to enter some words under some restrictions.

Your task is to modify the program so that these restrictions are checked. Your program should not raise any errors. You can assume that the user will always write something for each prompt (i.e. the input won't be an empty string).

Here are two examples of interactions that could take place.

```
Enter a string that begins with a vowel: Arkansas
Thanks!

Enter a string that ends with a consonant: potato
That doesn't end with a consonant.

Enter a 4-digit whole number: 1527
Thanks!

Enter an integer less than 50: 0
Thanks!
```

```
Enter a string that begins with a vowel: xyz123
That doesn't begin with a vowel.

Enter a string that ends with a consonant: 123ABC
Thanks!

Enter a 4-digit whole number: asdf
That's not a 4-digit whole number.

Enter an integer less than 50: no
That's not an integer less than 50.

```

Assume the following:
 * All zeroes at the beginning of a number are ignored 
 * `"y"` and `"Y"` do not count as vowels.
 * the user will NOT use letters with accents (e.g. É, ö, ç, ñ, etc.) or combined letters (e.g. œ, Æ, etc.)

**Hint: None of these problems require the use of a try-except.** (We'll learn about that later in this course.)

## Criteria
* The Input/Output Tests pass
* Your program must includes *at least two (2)* helpful line comments

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

Here is the original code in **main.py** for reference

```python
input1 = input("Enter a string that begins with a vowel: ")

# Complete this section so that it responds to input1

input2 = input("Enter a string that ends with a consonant: ")

# Complete this section so that it responds to input2

input3 = input("Enter a 4-digit whole number: ")

# Complete this section so that it responds to input3

input4 = input("Enter an integer less than 50: ")

# Complete this section so that it responds to input4
```
