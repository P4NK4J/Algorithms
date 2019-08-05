def minproduct(a,b,n,k): 
  
    diff = 0
    res = 0
    for i in range(n):  
  
        # Find product of current 
        # elements and update result. 
        pro = a[i] * b[i] 
        res = res + pro 
  
        # If both product and 
        # b[i] are negative, 
        # we must increase value 
        # of a[i] to minimize result. 
        if (pro < 0 and b[i] < 0): 
            temp = (a[i] + 2 * k) * b[i] 
  
        # If both product and 
        # a[i] are negative, 
        # we must decrease value 
        # of a[i] to minimize result. 
        elif (pro < 0 and a[i] < 0): 
            temp = (a[i] - 2 * k) * b[i] 
  
        # Similar to above two cases 
        # for positive product. 
        elif (pro > 0 and a[i] < 0): 
            temp = (a[i] + 2 * k) * b[i] 
        elif (pro > 0 and a[i] > 0): 
            temp = (a[i] - 2 * k) * b[i] 
  
        # Check if current difference 
        # becomes higher 
        # than the maximum difference so far. 
        d = abs(pro - temp) 
  
        if (d > diff): 
            diff = d        
    return res - diff 
  
# Driver function 
a = [ 2, 3, 4, 5, 4 ] 
b = [ 3, 4, 2, 3, 2 ] 
n = 5
k = 3
  
print(minproduct(a, b, n, k)) 
