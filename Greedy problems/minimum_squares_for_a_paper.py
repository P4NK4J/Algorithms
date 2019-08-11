# Returns min number of squares needed 
def minimumSquare(a, b): 
  
    result = 0
    rem = 0
  
    # swap if a is small size side . 
    if (a < b): 
        a, b = b, a  
  
    # Iterate until small size side is 
    # greater then 0 
    while (b > 0): 
      
        # Update result 
        result += int(a / b)  
  
        rem = int(a % b)  
        a = b  
        b = rem  
  
    return result  
  
# Driver code 
n = 13
m = 29
  
print(minimumSquare(n, m)) 
