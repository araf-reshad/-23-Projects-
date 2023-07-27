def num_roots(a, b, c):
    """Returns the number of real roots in the quadratic relation y = ax^2 + bx + c."""
  
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0: # There are two real roots
        return 2
    
    elif discriminant == 0: # There is one real root
        return 1
      
    else: # There are no real roots
        return 0