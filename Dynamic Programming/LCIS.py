def LCIS(arr1, n, arr2, m): 
  
    # table[j] is going to store length of LCIS 
    # ending with arr2[j]. We initialize it as 0, 
    table = [0] * m 
    for j in range(m): 
        table[j] = 0
  
    # Traverse all elements of arr1[] 
    for i in range(n): 
      
        # Initialize current length of LCIS 
        current = 0 

        #for each i traverse arr2[]
        for j in range(m): 
              
            # If both the array have same elements. 
            #  we don't break the loop here. 
            if (arr1[i] == arr2[j]): 
                if (current + 1 > table[j]): 
                    table[j] = current + 1
  
            # for current element of arr1[] seek previous smaller element 
            if (arr1[i] > arr2[j]): 
                if (table[j] > current): 
                    current = table[j] 
  
    # The maximum value in table[] is stored in result
    result = 0
    for i in range(m): 
        if (table[i] > result): 
            result = table[i] 
  
    return result

# Driver Code 
arr1 = [int(x) for x in input().split()]
arr2 = [int(y) for y in input().split()] 
  
n = len(arr1) 
m = len(arr2) 
  
print("Length of LCIS is", LCIS(arr1, n, arr2, m)) 
  

  
