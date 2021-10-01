from bisect import bisect_left

def fibonacciSearch(arr,x,n):
    # initialise fibonacci numbers
    fib2 = 0 # (m-2)th fibonacci no
    fib1 = 1 # (m-1)th fibonacci no

    fibM = fib1 + fib2 # store the smallest fibonacci number >= n

    while fibM < n:
        fib2 = fib1
        fib1 = fibM
        fibM = fib2 + fib1

    # marks the eliminated range from front
    offset = -1