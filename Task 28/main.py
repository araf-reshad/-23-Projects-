def merge_dictionaries(*dicts, **kwargs):
    """
    Merges multiple dictionaries together and returns it.
    When the same key appears in multiple dictionaries, 
    the value that appears in the earliest dictionary takes precedence, 
    unless the keyword argument `tiebreaker = "last"` is used, 
    in which case the value in the latest dictionary takes precedence.
    """
    # Check for unexpected keyword arguments
    if len(kwargs) > 1 or (len(kwargs) == 1 and 'tiebreaker' not in kwargs):
        raise KeyError("Unexpected keyword argument.")
    
    # Check for invalid values for the 'tiebreaker' keyword argument
    tiebreaker = kwargs.get('tiebreaker', 'first')
    if tiebreaker not in ['first', 'last']:
        raise ValueError("Invalid value for the 'tiebreaker' keyword argument.")
    
    # Merge the dictionaries
    merged_dict = {}
    if tiebreaker == 'first':
        for d in dicts:
            merged_dict = {**d, **merged_dict}
    else:
        for d in dicts:
            merged_dict = {**merged_dict, **d}
    
    return merged_dict

# Include at least five tests here.
d1 = {1: 2, 5: 10}
d2 = {5: 9}
d3 = {3: 4}

# Test 1
print(merge_dictionaries(d1, d2))  # should print {1: 2, 5: 10}
# Test 2
print(merge_dictionaries(d1, d2, tiebreaker="last"))  # should print {1: 2, 5: 9}
# Test 3
print(merge_dictionaries(d1, d2, d3, tiebreaker="last"))  # should print {1: 2, 3: 4, 5: 9}

# Test 4
try:
    print(merge_dictionaries(d1, d2, tiebreaker="middle"))
except ValueError as ve:
    print(ve)  # should print "Invalid value for the 'tiebreaker' keyword argument."
  
# Test 5
try:
    print(merge_dictionaries(d1, d2, unexpected_keyword="last"))
except KeyError as ke:
    print(ke)  # should print "Unexpected keyword argument."
