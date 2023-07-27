def positive_product(num_list):
  """Returns the product of all the positive numbers in num_list."""
  
  product = 1  #Initialize the product variable to 1
  
  for num in num_list: #Iterate through each element in the num_list
    
        if num > 0: #If the number is positive, multiply it with the current value of product
            product *= num
          
  return product #product of all positive numbers in num_list
