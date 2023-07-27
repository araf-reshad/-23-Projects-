def character_count(filepath):
  """Returns the number of characters in the Shakespeare play."""
  
  try:
    with open(filepath, "r") as f:
      
      content = f.read() #Read the entire content of the file 
      
      return len(content) # Return the number of characters in the file including whitespaces and newlines 
      
  except FileNotFoundError:
    return None

def word_count(filepath):
  """Returns the number of tokens in the Shakespeare play."""
  
  try:
    with open(filepath, "r") as f:
      
      content = f.read()
      
      words = content.split() #Split the content into words/token
      
      return len(words) #Return the no. of words/tokens in the file
      
  except FileNotFoundError:
    return


def line_count(filepath):
  """Returns the number of lines in the Shakespeare play."""
  
  try:
    with open(filepath, "r") as f:
      
      lines = f.readlines() #Read all lines of the file
      
      return len(lines) #Return no. of lines in the file
      
  except FileNotFoundError:
    
    return
