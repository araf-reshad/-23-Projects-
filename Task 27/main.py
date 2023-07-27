def consecutive_ints(*nums):
    """
    Takes any number of integer arguments and returns them in a sorted list if they can be arranged in a consecutive order.
    Otherwise raises a custom TypeError or ValueError.
    """
    
    # Check if the input is an integer only 
    if not all(type(n) is int for n in nums):
      raise TypeError("The inputs must be integers.")
      
    # Sort the numbers
    sorted_nums = sorted(nums)
    
    # Check if the numbers are consecutive
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] - sorted_nums[i - 1] != 1:
            raise ValueError("The inputs must be arrangeable in consecutive order.") 
    return sorted_nums

# Include at least three tests here that should return a list
print(consecutive_ints(4, 1, 3, 2))  # prints [1, 2, 3, 4]
print(consecutive_ints(-1, 0, 1))  # prints [-1, 0, 1]
print(consecutive_ints(10, 11, 12, 13))  # prints [10, 11, 12, 13]

try:
    # Test that should raise a TypeError
    print(consecutive_ints("4", "6", "1", "4")) 
except TypeError:
    print("This raises a TypeError.")
except:
    print("This raises the wrong error.")

try:
    # Test that should raise a ValueError
    print(consecutive_ints(999,888,666,555))
except ValueError:
    print("This raises a ValueError.")
except:
    print("This raises the wrong error.")