def list_counts(lst1, lst2, lst3):
  """Returns a dictionary in which:
  - the keys are all the items that appeared in the lists 
  - the values are the number of lists that the item appeared in
  """
  all_lsts = [set(lst1), set(lst2), set(lst3)]
  
  answer = dict()
  
  for lst in all_lsts:
    
    for item in lst:
      
      # We increase the value of the key for each list the key is found in
      
      if item in answer:
        answer[item] += 1
        
      else:
        answer[item] = 1
        
  return answer


# Test 1
# Should print 'True'
lst_1_test_1 = [1, 2, 3, 4]
lst_2_test_1 = [-1, 2, -3, 4]
lst_3_test_1 = [-1, 2, 3, -4]
answer_test_1 = {-4: 1, -3: 1, -1: 2, 1: 1, 2: 3, 3: 2, 4: 2}
print(list_counts(lst_1_test_1, lst_2_test_1, lst_3_test_1) == answer_test_1)

# Test 2
# Should print 'True'
lst_1_test_2 = [1, 2, 3, 4]
lst_2_test_2 = [1, 2]
lst_3_test_2 = []
answer_test_2 = {1: 2, 2: 2, 3: 1, 4: 1}
print(list_counts(lst_1_test_2, lst_2_test_2, lst_3_test_2) == answer_test_2)

# Test 3
# Should print 'True'
lst_1_test_3 = [5, 4, 3, 2, 1]
lst_2_test_3 = [1, 23, 4, 5]
lst_3_test_3 = [12, 34, 5]
answer_test_3 = {1: 2, 2: 1, 3: 1, 4: 2, 5: 3, 12: 1, 23: 1, 34: 1}
print(list_counts(lst_1_test_3, lst_2_test_3, lst_3_test_3) == answer_test_3)

# Test 4
# Should print {}
print(list_counts([], [], []))

