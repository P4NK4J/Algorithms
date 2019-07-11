n=3
def findLongestFromACell(i, j, mat, dp): 
    # Base case  
    if (i<0 or i>=n or j<0 or j>=n): 
        return 0
  
    # If this subproblem is already solved  
    if (dp[i][j] != -1):  
        return dp[i][j] 
  
    # Since all numbers are unique and in range from 1 to n*n,  
    # there is atmost one possible direction from any cell  
    if (j<n-1 and ((mat[i][j] +1) == mat[i][j+1])): 
        dp[i][j] = 1 + findLongestFromACell(i,j+1,mat,dp) 
        return dp[i][j] 
  
    if (j>0 and (mat[i][j] +1 == mat[i][j-1])):  
        dp[i][j] = 1 + findLongestFromACell(i,j-1,mat,dp) 
        return dp[i][j] 
  
    if (i>0 and (mat[i][j] +1 == mat[i-1][j])): 
        dp[i][j] = 1 + findLongestFromACell(i-1,j,mat,dp) 
        return dp[i][j]  
  
    if (i<n-1 and (mat[i][j] +1 == mat[i+1][j])): 
        dp[i][j] = 1 + findLongestFromACell(i+1,j,mat,dp) 
        return dp[i][j] 
  
    # If none of the adjacent fours is one greater  
    dp[i][j] = 1
    return dp[i][j] 
  
  
# Returns length of the longest path beginning with any cell  
def finLongestOverAll(mat): 
    result = 1 # Initialize result  
  
    # Create a lookup table and fill all entries in it as -1  
    dp=[[-1 for i in range(n)]for i in range(n)] 
  
    # Compute longest path beginning from all cells  
    for i in range(n): 
        for j in range(n): 
            if (dp[i][j] == -1): 
                findLongestFromACell(i, j, mat, dp) 
            # Update result if needed  
            result = max(result, dp[i][j]);  
    return result 
  
# Driver program  
mat = [[1, 2, 9],  
    [5, 3, 8], 
    [4, 6, 7]]  
print("Length of the longest path is ",finLongestOverAll(mat))

