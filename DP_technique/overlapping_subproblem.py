'''
As term 'Overlapping' hints, we have same overlapping (duplicates) computation for multiple recursions

- Basically, we have complex recursive calls
- Each recursive function may be called more than one times.
'''

## -- Example 01 --

# Fibbonacci Series
# 1, 1, 2, 3, 5, 8, 13, 21
# First two terms are both 1
# Each subsequent term is sum of previous two terms.
# Fib(1) = Fib(2) = 1 if n = 1, 2
# Fib(n) = Fib(n-1) + Fib(n-2) if n > 2

def fib(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# Consider fib(5)
'''
                                fib(5)
                        
                    fib(4)                  fib(3)

            fib(3)        fib(2)    fib(2)           fib(1)

       fib(2)    fib(1)

       
The equation of time taken by the function:

T(n) = T(n-1) + T(n-1) + O(1)

- This an equation for exponential time.
- Because this solves the same subproblems multiple times which is inefficient approach in terms of time and memory.
'''                


## -- Example 02 --

# There are N stations in a route, starting from 0 to N-1.
# A train moves from 1st station to last station N-1 in only forward direction. 
# The cost of ticket between any stations is given,
# Find the minimum cost of travel from station 0 to station N-1.

'''
We need to define the data structure in which cost of ticket between
stations is stored.

Let's assume there're 4 stations: (0-3)
0 -> 1 -> 2 -> 3

Then cost of ticket is stored in a 4 x 4 matrix:

cost[4][4] = [[0, 10, 75, 94],
              [-1, 0, 35, 50],
              [-1, -1, 0, 80],
              [-1, -1, -1, 0]]

cost[i][j] is cost of ticket from station i to station j.
Since we are not going backward,
cost[i][j] does not make sense when i > j, hence all are -1.
If i == j, we are at the same station.


- Moving from station 0 -> station 2:
    cost = 75, if 0 -> 2 directly
    cost = 10 + 35, if 0 -> 1, 1 -> 2

- We need to find minimum cost of travel from station 0 to station 3

Let's say minCost(s, d) is minimum cost of traveling from station s to station d

minCost(0, N-1) = MIN (
                    cost[0][N-1]
                    cost[0][1] + minCost(1, N-1)
                    cost[0][2] + minCost(2, N-1)
                    cost[0][3] + minCost(3, N-1),
                    ...........................,
                    cost[0][i] + minCost(i, N-1),
                    ...........................,
                    cost[0][N-1] + minCost[N-1, N]
                  )

01. First option -> Go directly to station N-1 from station 0 without any break
    >> cost[0][N-1]
02. Second option -> Having breaks in between station 0 and station N-1
    >> cost[0][i] + cost[i][N-1]

There are two termination conditions:
01. when both stations are same
    If s == d: return 0

02. when s is just before d, there is only one way to reach d from s
    If s == d-1: return cost[s][d]

Both of those conditions can be combined to one condition:
(when s==d cost is set to zero)

    If (s == d | s == d-1): return cost[s][d]


'''

def minCostStation(N=4):
    if N > 4:
        raise ValueError('Not implemented for number of stations > 4')
    # cost matrix for 4 stations
    cost = [[0, 10, 75, 94],
            [-1, 0, 35, 50],
            [-1, -1, 0, 80],
            [-1, -1, -1, 0]]
    
    def calculate_minCost(s, d):
        # base condition
        if s == d | s == d-1: 
            return cost[s][d]

        min_cost = cost[s][d]
        # try every intermediate station to find min cost
        for i in range(s+1, d, 1):
            # min cost of going from s to i + min cost of going from i to d
            temp = calculate_minCost(s, i) + calculate_minCost(i, d)
            if temp < min_cost:
                min_cost = temp
        return min_cost

    return calculate_minCost(0, N-1)

'''
This problem adheres to the optimal substructure property, because we are computing
the min cost of travel between intermediate stations to find the actual min cost
of going from initial source to final destination.

Although this implementation solves subproblems multiple times:

                        0, 3
        [0, 1    1, 3]          [0, 2   2, 3]
                [1, 2   2, 3]    
'''
