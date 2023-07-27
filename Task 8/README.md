## Before Starting This Task

It's recommended that you **only begin this task if you have already submitted Task #7.** It's okay if you are waiting for it to be reviewed.

Choose between watching all the videos or reading all of the notes.

* [Importing Modules](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.27%20Importing%20Modules.md) 
* [The `random` Module](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.28%20The%20random%20Module.md) 
* [While Loops](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.29%20While%20Loops.md) 
* [The `pass` Keyword](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%201/1.30%20The%20pass%20Keyword.md)

## Instructions

Create a program that generates a random integer from 1 to 100 then prompts the user to guess it. 
* If they guess correctly on the first try, it prints: `"WOW! You won in 1 guess! The number was _."` (fill in the blank with the number).
* If they guess correctly in 2 to 7 tries, it prints: `"You won in _ guesses! The number was _."` (fill in the blanks).
* If they guess incorrectly it says `"Higher!"` or `"Lower!"`.
* If they don't guess it within 7 tries it says `"Better luck next time. The number was _."` (fill in the blank with the number).
* At any point if they guess something other than an integer from 1 to 100, it says `"Invalid guess. Try again."` and it doesn't count as a try.

See the examples below for the remaining prompts.

```
Guess the number from 1 and 100!
Enter guess #1: 38
Higher!
Enter guess #2: 84
Lower!
Enter guess #3: 70
Lower!
Enter guess #4: 45
Lower!
Enter guess #5: 42
You won in 5 guesses! The number was 42. 
```
```
Guess the number from 1 and 100!
Enter guess #1: 87
Lower!
Enter guess #2: 75
Lower!
Enter guess #3: 200
Invalid guess. Try again.
Enter guess #3: 30
Higher!
Enter guess #4: 45
Higher!
Enter guess #5: 54
Higher!
Enter guess #6: 67
Lower!35
Enter guess #7: 60
Lower!
Better luck next time. The number was 61.
```

## Criteria
* Your program runs the game exactly as described
* Your program uses the prompts from the examples (the numbers will be different from the examples because the secret number is random and you get to choose your seven guesses)
* Your program uses at least one loop
* Your program doesn't have an infinite loop

There are no Input/Output tests, so you should carefully test your program by playing it to ensure that everything works as expected.

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

## main.py

The **main.py** file is initially blank for this task.
