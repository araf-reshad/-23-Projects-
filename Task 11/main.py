def round_numbers(mixed_list):
    """Returns a new list with all numbers from mixed_list rounded to the nearest 10 and all non-numeric values removed."""
   
    new_list = []
  
    for item in mixed_list:
      
        if (type(item) == int or type(item) == float):
          multiplier = -1 if item < 0 else 1
          
          item = abs(item) #absolute value function to remove the sign
          
          last_digit = item % 10 #calculate last digit of the item by taking modulo 10 of item
          
          if last_digit >= 5:
            new_list.append((item + 5) // 10 * 10 * multiplier)
       
          else:
            new_list.append(item// 10 * 10 * multiplier) #Round the item to the nearest multiple of 10 based on the last digit, then append to new_list while preserving the original sign.
            
    return new_list

#Tests
print(round_numbers([]))  # should print []
print(round_numbers(["hi", True, "koala"]))  # should print []
print(round_numbers([1]))  # should print [0]
print(round_numbers([-15, "x", False]))  # should print [-20]
print(round_numbers([-0.1, 0, 1.8, "abc",
                     13.6]))  # should print [0.0, 0, 0.0, 10.0]
print(round_numbers([1, 11, 15, 21, 40,
                     99]))  # should print [0, 10, 20, 20, 40,  100]
print(round_numbers([-25, -15.0, -5, 0, 5.0,
                     15]))  # should print [-30, -20.0, -10, 0, 10.0, 20]

print(round(4.5))