import random

guess_num = 1

print ("Guess the number from 1 and 100!")

answer_num = random.randint(1, 100)  #Python picks the answer as a random number between 1 and 100

while True: 
    user_input = input("Enter guess #" + str(guess_num) + ": ")

    if not user_input.isdecimal() or int(user_input) < 1 or int(user_input) > 100: #Keeps prompting user to enter valid input
      print("Invalid guess. Try again.")  

      continue

    user_input = int(user_input)

    if (guess_num==1) and (user_input==answer_num):
      print ("WOW! You won in 1 guess! The number was " + str(answer_num) + ".") #number is guessed correctly in 1 guess

    elif user_input == answer_num:
      print("You won in " + str(guess_num) + " guesses! The number was " + str(answer_num) + ".")
      
      break #if answer is guessed correctly, the game ends 

    elif user_input < answer_num:
      print("Higher!")

    else:
      print("Lower!")

    guess_num += 1  #increases guess number (counter) by 1 after each guess

    if guess_num > 7:
      print("Better luck next time. The number was " + str(answer_num) + ".")

      break
