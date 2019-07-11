<<<<<<< HEAD
def printCountDP(dist): 
    count = [0] * (dist + 1) 
      
    # Initialize base values. There is 
    # one way to cover 0 and 1 distances 
    # and two ways to cover 2 distance 
    count[0] = 1
    count[1] = 1
    count[2] = 2
      
    # Fill the count array in bottom 
    # up manner 
    for i in range(3, dist + 1): 
        count[i] = (count[i-1] + 
                   count[i-2] + count[i-3]) 
          
    return count[dist]; 
  
# driver program
print("enter the score or distance")
dist = int(input()) 

print( printCountDP(dist)) 
=======
def printCountDP(dist): 
    count = [0] * (dist + 1) 
      
    # Initialize base values. There is 
    # one way to cover 0 and 1 distances 
    # and two ways to cover 2 distance 
    count[0] = 1
    count[1] = 1
    count[2] = 2
      
    # Fill the count array in bottom 
    # up manner 
    for i in range(3, dist + 1): 
        count[i] = (count[i-1] + 
                   count[i-2] + count[i-3]) 
          
    return count[dist]; 
  
# driver program
print("enter the score or distance")
dist = int(input()) 

print( printCountDP(dist)) 
>>>>>>> beb84f15930a32dbc97f1ee41d9332b0a1adfa27
