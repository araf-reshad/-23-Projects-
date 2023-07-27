def set_of_duplicates(lst):
  """Returns the set of all duplicate items in lst."""
  
  # What goes here?
  duplicate_set = set() # Create an empty set 
  
  for item in lst: 
    # If element is a duplicate, add it to the set 
    if lst.count(item) > 1: 
      duplicate_set.add(item)
  return duplicate_set
        

# These 3 lists will be used for testing
list_1 = [1,1,2,3,2,4,5,99,3,1]
list_2 = [-5,-4,-3,-2,-1]
list_3 = [1,2,3,4,5,5,4,3,2,1]

# The following 3 tests should print 'True'
print(set_of_duplicates(list_1) == {1,2,3}) 
print(set_of_duplicates(list_2) == set()) 
print(set_of_duplicates(list_3) == {5,2,3,1,4})

print(set_of_duplicates([])) # Should print set()
