 ### -- Recursion -- ###
'''
Recursion should contains following main 02 properties:

01. Terminal state - where the operation ends.
02. Do some operation and call to the function itself.

In each call we try to do the same computation with reduced amount of inputs
'''

# examples

def sum_num(x):
    if x == 0: return 0
    if x == 1: return 1

    return x + sum_num(x-1)

def pow(x, n):
    if n == 0: return 1
    if x == 1: return 1
    return x * pow(x, n-1)



'''

How to solve a problem using recursion

- Define the large problem in terms of smaller problems of same type
- Focus on smaller problem and solve it first, then pass the reduced input to recursive call

'''



# Recursive Implementation of Bubble Sort
# -- Iterative solution
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# -- Recursive solution
def bubbleSort_re(arr, n):
    if n == 0: return  

    # perform one pass
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    # recursive call
    bubbleSort_re(arr, n-1)
    # print(arr)
    return arr


# print(bubbleSort([30, 3, 1]))
# print(bubbleSort_re([30, 3, 1, 6], 4))



'''
Head Recursion Vs Tail Recursion

- Head Recursion -> if recursive call is made before it performs its own task
- Tail Recursion -> if recursive call is made at the end of the function

Tail recursion is easy to write as a loop

'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Head Recursion
def traverse(head):
    if head:
        traverse(head.next)
        print(head.data)


# Tail Recursion
def traverse(head):
    if head:
        print(head.data)
        traverse(head.next)


# Combination of head and tail recursion
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inOrder(node: Node):
    if not node: return

    inOrder(node.left)
    print(node.data)
    inOrder(node.right)
