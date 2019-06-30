print("enter string 1")
x  =  input()

print("enter string 2")
y = input()

m = len(x)
n = len(y)

"""function printing LCS of x and y """
def lcs(x,y,m,n):

    l = [[0 for x in range(n+1)]for x in range(m+1)]
    """ l contains length of LCS of x and y """

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :            
                l[i][j] = 0       
            elif x[i-1] == y[j-1]:
                l[i][j] = (l[i-1][j-1]) + 1         #diagonal element + 1
            else:
                l[i][j] = max(l[i-1][j] , l[i][j-1])

    # Following code is used to print LCS 

    index = l[m][n] #stores length of lcs

    lcs = [""] * (index+1) #char array to store lcs string
    lcs[index] = "" 
  
    i = m            #start from the rightmost corner then traceback  
    j = n 
    while i > 0 and j > 0: 
  
        # If current character in X[] and Y are same, then 
        # current character is part of LCS 
        if x[i-1] == y[j-1]: 
            lcs[index-1] = x[i-1] 
            i -= 1
            j -= 1
            index -= 1
  
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
        elif l[i-1][j] > l[i][j-1]: 
            i -= 1
        else: 
            j -= 1
  
    print("LCS of " + x + " and " + y+ " is " + "".join(lcs))


"""Driver's program"""

print("enter string 1")
x  =  input()

print("enter string 2")
y = input()

m = len(x)
n = len(y)
lcs(x,y,m,n)
  
                
    
