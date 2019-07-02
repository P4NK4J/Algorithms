# Python 3 program to find Edit Distance
# (when only two operations are allowed, insert and delete) using LCS.

def editDistanceLCS(X, Y):

# Find LCS
    m = len(X)
    n = len(Y)
    L = [[0 for x in range(m + 1)] for y in range(n + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
        
            if  i == 0 or j == 0:
                L[i][j] = 0
            elif  X[i-1] == Y[j-1] :
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    lcs = L[m][n]
    douche = ((m-lcs)+(n-lcs))

    return douche

"""Driver Program"""

X = input()
Y = input()

print("number of edits required are", editDistanceLCS(X, Y))

