# lis returns length of the longest increasing subsequence in arr of size n 
def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and initialize list with "1"
    lis = [1]*n 
  
    # compute length of LIS ad
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
  
    # Initialize maximum to 0 to get the maximum of all 
    # LIS 
    maximum = 0
  
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , lis[i]) 
  
    return maximum 
<<<<<<< HEAD

"""driver program"""

=======
#driver program
>>>>>>> a68baaec47a29c58b14c26c37be0bc3c03f33906
arr = [int(x) for x in input().split()]

# c is the length of LIS in the input array
c = lis(arr)  
print(c)
