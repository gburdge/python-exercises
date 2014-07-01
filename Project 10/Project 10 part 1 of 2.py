# # This is a classical example of recursion, but inefficient!
# # Consider the Fibonacci algorithm:
def naive_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return naive_fib(n-1) + naive_fib(n-2)
 # find a way to save the previous Fibonacci values, n-1 and n-2, ensuring
 # that we're not repeating work we've already done.
 # This can be accomplished using a recursive helper function, as shown below:
def fib_helper(n):
    if n == 0:
        return 0
    else:
        return fib_improved(n, 0, 1)

def fib_improved(n, p0, p1):
    if n == 1:
        return p1
    else:
        return fib_improved(n-1, p1, p0 + p1)

# The goal of part 1 is to have you benchmark these two functions