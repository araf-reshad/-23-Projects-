height = input("Enter an integer between 1 and 5: ")

if not height.isdecimal() or int(height) < 1 or int(height) > 5: 
  
    print("That's not an integer between 1 and 5.") #stops program if height is not valid 
  
else:
  
    for i in range(1, int(height) + 1): 
      
        print(' ' * (2 * (int(height) - i)), end='') #prints leading spaces and stays on same line 
      
        for j in range(i, 2 * i): #prints the numbers in each line
            print(str(j)+' ', end='') 
  
        print() #goes to new line

      
   
