'''
Function to calculate n'th fibonacci number is actually a dynamic programming solution.
- We go in a bottom-up manner: starting from fib(1) and fib(2) and so on
'''

# 1, 1, 2, 3, 5 ....
# a  b  c
#    a  b

def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    
    # for (k-2)'th term
    # for (k-1)'th term
    # for k'th term
    a, b, c = 1, 1, 0

    for _ in range(3, n):
        c = a + b
        a, b = b, c
    return c

'''
- Both Memoization and DP solves individual subproblem only once.
- Memoization uses recursion and work top-down, while DP moves in bottom-up
- DP doesn't use any recursion as it unrolls recursion part!
'''

# -- Another implementation to fib --
# This is also a DP
def fib(n: int) -> int:
    # Arrays to store fib numbers
    arr = [0] * (n + 1)

    arr[1], arr[2] = 1, 1

    for i in range(3, n+1):
        # compute fib(n) and store it
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]