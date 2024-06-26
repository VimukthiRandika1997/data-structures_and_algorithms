'''
Input: [4, 2, 9, 7, 5, 6, 7, 1, 3], k = 4
Output: 6

Find the K'th largest element in the array and return it

1st largest element: 9
2nd largest element: 7
3rd largest element: 7
4th largest element: 6

'''

# Approach 1: Remove maximum element (k-1) times and return largest remaining element!
'''

[4, 2, 9, 7, 5, 6, 7, 1, 3], k = 4

Iter 01: [4, 2, 7, 5, 6, 7, 1, 3], 9 is removed
Iter 02: [4, 2, 5, 6, 7, 1, 3], 7 is removed
Iter 03: [4, 5, 6, 1, 3], 7 is removed
return largest remaining element: 6

'''

def kth_largest(arr: list, k: int) -> int:
    for i in range(k-1):  # k-1
        arr.remove(max(arr)) # n(worst case shifting elements in array) + n(finding max element in array)
    return max(arr) # n(max element in the remain)

'''
Total time complexity: (k-1) * 2n + n = 2kn + n = O(kn)
Space complexity: O(1)
'''

# Approach 2: Sort the array first, find the kth element after that!
'''
[4, 2, 9, 7, 5, 6, 7, 1, 3], k = 4

[1, 2, 3, 4, 5, 6, 7, 7, 9]
'''
def kth_largetst(arr: list, k: int) -> int:
    n = len(arr)
    arr.sort() # nlogn
    return arr[n-k]

'''
Time complexity: O(nlogn) 
Space complexity: O(1)

'''

# Approach 3: Base on a priority queue, remove the element with highest priority(largest element)
# 01. create the priority queue: using max heap or min heap
# 02. for i in K:
#       remove the element with highest priority (largest element)

'''



'''

def kth_largest(arr: int, k: int) -> int:
    import heapq
    # since heapq in python is a min-heap implementation
    arr = [-ele for ele in arr]
    # create the min-heap
    heapq.heapify(arr)
    # remove lowest(highest in this case) k-1 times from the heap
    for _ in range(k-1):
        heapq.heappop(arr)
    return heapq.heappop(arr) # k'th element

'''

Total time complexity: n + n + (k-1) * logn + logn = 2n + klogn =  O(klogn)

if k is closer to n => O(n + klogn) = O(nlogn)
if k is closer to zero => O(n + klogn) = O(n)

'''
