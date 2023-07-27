#Write results into text file "sums.txt"
with open("sums.txt", "w") as f:

# Iterate through each number from 1 to 100 (inclusive)
  for i in range(1, 101):

    #Variable to keep track of if we've found a sum for current i
    found = False
    
    #Iterate through each number from 1 to i
    for n in range (1, i):
      seq_sum=0
      
      #Start summing from n until you reach or exceed i
      for m in range (n,i):
        seq_sum += m
        
       #If the sum of our sequence equals i, we've found a valid sum
        if seq_sum == i: 
          
          #If a sum is found, write it to file and set 'found' variable to True    
          f.write(f"{i} = {' + '.join(str(x) for x in range (n, m+1))}\n")
          found = True 
          break 

      #If sum of our sequence is greater than i, we stop adding numbers and break the loop
        elif seq_sum > i: 
          break

      #If sum of our sequence is valid, we break the outer loop and move to the next number i
      if found: 
        break

    #If no valid sum was found for the current i
    if not found: 
      
      f.write(f"{i} is NOT possible.\n")

