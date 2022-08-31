''' Fibonacci Function '''


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' \n')
        a, b = b, a+b
    print("\n")


print(fib(10**10000000))
