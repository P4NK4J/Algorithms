def editDist(str1, str2, m, n): 

    """ Create a table to store results of subproblems"""
    table = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    """bottom up approach table filling from tree""" 
    for i in range(m+1): 
        for j in range(n+1): 
  
            """comparison of each string with "fi" """
            if i == 0: 
                table[i][j] = j    # Min. operations = j 
  
            elif j == 0: 
                table[i][j] = i    # Min. operations = i 
  
                """ If last characters are same, ignore last char 
                 and recur for remaining string . due to addition of fi
                 in table str[i-1] is taken for a match """
            elif str1[i-1] == str2[j-1]: 
                table[i][j] = table[i-1][j-1] 
      
                """If last character are different, consider all 
                 possibilities and find minimum and add 1 to it"""
            else: 
                table[i][j] = 1 + min(table[i][j-1],    # Insert 
                                   table[i-1][j],       # Remove 
                                   table[i-1][j-1])     # Replace 
  
    return table[m][n]

"""Driver,s Program"""
str1 = input()
m = len(str1)

str2 = input()
n = len(str2)

edit = editDist(str1, str2, m, n)
print("number of operations required are", edit)
