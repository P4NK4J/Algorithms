# fibonacci function
def fib(n):
    temp = [0] * (n+1)
    temp[0] = 0
    temp[1] = 1
    for i in range(2,n+1):
        temp[i] = temp[i-1] + temp[i-2]
    return temp[n]

""" Driver Program """
print("The Fifth Number of Fibonacci sequence is :")
print(fib(5))
