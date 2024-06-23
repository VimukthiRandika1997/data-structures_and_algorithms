'''
Recursive solution may be solving the same subproblem multiple times.
This would lead to take time complexity of the code to exponential levels.

In memoization, we store the solution of a subproblem in some sort of a cache when it is solved for the first time.
- When the same subproblem is encountered again, then the already solved result is returned from the cache.
'''

## -- Example 01 --
# Fibonacci series: 1 1 2 3 5 .....
def fib(n: int):
    # this array will store fib(k) at k'th index
    # memo[k] == 0 means fib(k) is not yet calculated
    memo = [0] * (n+1)

    def calculate_fib(n):
        # fib(n) is already calculated, don't compute again!
        if memo[n] != 0:
            return memo[n]
        # compute fib(n) and store in the cache
        if n == 1 or n == 2:
            memo[n] = 1
        else:
            memo[n] = calculate_fib(n-1) + calculate_fib(n-2)
        return memo[n]

    return calculate_fib(n)

# print(fib(8))

'''
Function fib(n) will call itself recursively only when it is called for the first time for n,
in subsequent calls for the same value will be taken by looking up the array!

There are two types of call to the function:
    01. one that does actual computation and hence may call itself recursively (non-memoized call)
    02. other just do a look-up in the array and hence return already stored result (memoized call)

There will be exactly O(n) non-memoized calls and each call takes constant time,

                                fib(5)
                        
                    fib(4)                  fib(3)

            fib(3)        fib(2)    fib(2)           fib(1)

       fib(2)    fib(1)

the reason is because fib(4) and fib(3) are already calculated, then non-memoized call of fib(5)
will add those two and takes constant time.

Hence we have optimized an exponential time function to take linear time using simple cache mechanism!!!
'''


# -- Example 2 --
# Previous example in overlapping subproblems
# Minimum cost for going station-s to station-d

'''
Since this subproblem has two parameters: s and d,
the cache can not be stored in 1D array, we need 2D array


we take 2D array of size N*N as cache to stores minimum cost of traveling between two stations
memo[N][N] = initialize to 0

- Once the minimum cost is computed for traveling from station-s to station-d,
  this value is stored in cell memo[s][d].

- Next time when the function is called with same parameters (to compute min cost from s to d),
  we do not compute the min cost again and just return the valued stored in the cache memo[s][d]
  which is a constant time operation!


*** Note ***

- Deciding data structure of cache is important step in memoization.
- The cache should be capable of storing results of all subproblems.

- Usually cache is an array.
- If your problem has only one dimension -> then it is 1D array
- Else it is a multi-dimensional array

'''

def minCostStation(N=4):
    if N > 4:
        raise ValueError('Not implemented for number of stations > 4')
    # cost matrix for 4 stations
    cost = [[0, 10, 75, 94],
            [-1, 0, 35, 50],
            [-1, -1, 0, 80],
            [-1, -1, -1, 0]]
    
    # cache to store already computed results
    memo = [[0] * (N+1)] * (N+1)
    
    def calculate_minCost(s, d):
        # base condition
        if s == d or s == d-1: 
            return cost[s][d]
        # compute if value is not yet computed
        if memo[s][d] == 0:
            min_cost = cost[s][d]
            # try every intermediate station to find min cost
            for i in range(s+1, d, 1):
                # min cost of going from s to i + min cost of going from i to d
                temp = calculate_minCost(s, i) + calculate_minCost(i, d)
                if temp < min_cost:
                    min_cost = temp
            # store the min_cost in cache for later use
            memo[s][d] = min_cost
        return memo[s][d]

    return calculate_minCost(0, N-1)

# print(minCostStation(4))


'''
Memoization is a top-down approach

Memoization = Recursion + Cache - Recomputing overlapping subproblems
'''