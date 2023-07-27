# Input_1

input_1 = input("Enter a string that begins with a vowel: ")

input_1 = input_1.upper() #Using .upper() to turn all characters into upper-case. Makes code more effective/easier since we only have to check for upper-case vowels. 

if input_1[0] == 'A' or input_1[0] == 'E' or input_1[0] == 'I' or input_1[0] == 'O' or input_1[0] == 'U':
    print("Thanks!")
  
else:
    print("That doesn't begin with a vowel.")

  
# Input_2
  
input_2 = input("Enter a string that ends with a consonant: ")

input_2 = input_2.upper()

last_letter = input_2[len(input_2) - 1] #holds the last letter of the string

if last_letter > 'A' and last_letter <= 'Z' and not (last_letter == 'E' or last_letter == 'I' or last_letter == 'O'or last_letter == 'U'): #checks if last letter is a consonant 
    print("Thanks!")
  
else:
    print("That doesn't end with a consonant.")

  
# Input_3
  
input_3 = input("Enter a 4-digit whole number: ")

if input_3.isdecimal() and int(input_3) < 10000 and int(input_3) > 999:
    print("Thanks!") #checks if input is a valid number (the string only contains numbers) and if it is 4 digits long
  
else:
    print("That's not a 4-digit whole number.")


# Input4
  
input_4 = input("Enter an integer less than 50: ")

if input_4[0] == '-' and input_4[1:].isdecimal(): #checks if input is a valid negative number (string only contains negative sign and numbers)
    print("Thanks!")
  
elif input_4.isdecimal() and int(input_4) < 50:
    print("Thanks!")
  
else:
    print("That's not an integer less than 50.")
