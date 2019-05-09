MAX = 100
# initialization of lookup array with NULL
lookup = [0] * MAX

# fibonacci function
def fib(n):
    if lookup[n] == 0:
        if n <= 1:
            lookup[n] = n
        else:
            lookup[n] = fib(n-1) + fib(n-2)
    return lookup[n]

""" Driver Program """
print("The Fifth Number of Fibonacci sequence is :")
print(fib(5))
