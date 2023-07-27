## Before Starting This Task

**It's recommended that you only begin this task if you have already submitted Task #11.** It's okay if you are waiting for it to be reviewed.

Choose between watching all the videos or reading all of the notes.

* Scope ([video](https://www.youtube.com/watch?v=AuftMb-SybU&list=PLVD25niNi0BkyCc47RgZHKnmIh6nsupN7)|[note](https://github.com/Kitchener-Waterloo-Collegiate-and-VS/ICS3U/blob/main/Unit%202/2.09%20Scope.md))

## Instructions

Complete the functions `play_rps()` and `display_score()` in **main.py** according to their documentations.

Here is an example game:

```
My wins: 0
Bot wins: 0
Ties: 0
Enter 'rock', 'paper', or 'scissors': rock
You chose rock.
Bot chose scissors.
You win!
My wins: 1
Bot wins: 0
Ties: 0
Enter 'rock', 'paper', or 'scissors': paper
You chose paper.
Bot chose scissors.
Bot win!
My wins: 1
Bot wins: 1
Ties: 0
Enter 'rock', 'paper', or 'scissors': paper
You chose scissors.
Bot chose scissors.
It's a tie!
My wins: 1
Bot wins: 1
Ties: 1
Enter 'rock', 'paper', or 'scissors': quit
Okay, bye.
```

There are no unit tests for this exercise. Test your program by playing the game.

## Criteria
* Your program runs the game exactly as described
* The docstrings were not moved or removed
* Your `play_rps()` function includes *at least one (1)* helpful line comment (the docstring doesn't count for this)

&nbsp;&nbsp;

When these criteria are met and you answer the questions in **sources.md**, you may submit this assignment.

If you submit this task without meeting these criteria, you will be asked to redo it and resubmit it.

### main.py

Here is the original code in **main.py** for reference:

```python
my_wins = 0
bot_wins = 0
ties = 0
game_over = False

def play_rps():
  """Simulates one round of rock-paper-scissors.
  
  First, it prompts the user to enter "rock", "paper", or "scissors". If the user enters "quit", the game ends (game_over becomes True). If the user enters anything else, it prompts them again. 
  
  If the user didn't quit, the bot is assigned "rock", "paper", or "scissors" at random.

  Then, it displays the user's move and the bot's move and says who won the round. The three global variables that keep track of the score are updated.
  """
  # What goes here?
  pass # Delete this line when you're done

def display_score():
  """Displays the score in the following format:
  My wins: _
  Bot's wins: _
  Ties: _
  """
  # What goes here?
  pass # Delete this line when you're done

# Don't modify anything below here
while not game_over:
  display_score()
  play_rps()
```
