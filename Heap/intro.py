'''
The heap is a tree data structure where each node is smaller than or equal
to its children if it is a min-heap or

greater than or qual to its childern if it's a max-heap, depending on the type.

Min Heap
                                    3
                    6                           4
            9               12          8               7
        14      15      13      18  11      9

- The root is the smallest element 


Max Heap

                                17
                    14                       16
            11           12         12               13
        6      5      7      2  9       11

        
- The root is the highest element
'''



'''
        ##-- Binary Heap --##

- The binary heap is a complete binary tree that respects the heap property

- Complete binary tree:
    
    A binary tree where every level is completely filled except maybe the last one,
    but all its nodes have to be as far to the left as possible.

- Heap property:

    Each node is smaller than or equal to its children if it's a min-heap.

    Each node is greater than or equal to its children if it's a max-heap.


'''


'''

Typically, Binary Tree is stored in a Node-wise manner

Class Tree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


But if the Binary Tree is a complete tree, then it can be stored in a array
    - This is because it is efficient to store in that way, we can access left and right elements quickly

                                    3
                    6                           4
            9               12          8               7
        14      15      13      18  11      9

    
    [3, 6, 4, 9, 12, 8, 7, 14, 15, 13, 18, 11, 9]

    For a given Node i,
        Left child: 2i + 1
        Right child: 2i + 2
        Parent: (i-1) / 2

    [3, 6, 4, 9, 12, 8, 7, 14, 15, 13, 18, 11, 9]
        i-1       i                2i+1 2i+2

'''


'''

Main Binary Heap Operations:

    Insert
    get_min / get_max
    extract min / max
    update
    build

    
There are two main sub-operations to maintain the heap property:

    01. Shift-up: bring the node up to a parent
    02. Shift-down: bring the node down to a child
'''

# Shift up
def _shift_up(self, i):
    parent = (i - 1) // 2

    # as long as node is not the root and less than the parent node value
    while i != 0 and self.heap[i] < self.heap[parent]:
        # swap the values with parent
        self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
        # change the index
        i = parent
        parent = (i - 1) // 2


# Shift down
def _shift_down(self, i):
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    while ( left_index < len(self.heap) and self.heap[i] > self.heap[left_index]) \
          or ( right_index < len(self.heap) and self.heap[i] > self.heap[right_index]):
        
        smallest = left_index if (right_index >= len(self.heap) or self.heap[left_index] < self.heap[right_index]) else right_index
        # swap nodes
        self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
        i = smallest
        left_index = 2 * i + 1
        right_index = 2 * i + 2

'''

Binary Heap is a complete tree. Hence both shift-up and shift-down operations would take O(log n) time

'''

# Insert method: O(log n)
def insert(self, element):
    self.heap.append(element)
    self._shift_up(len(self.heap) - 1)


# Getting minimum value in the heap
def get_min(self):
    return self.heap[0] if len(self.heap) > 0 else None


# Extract min value: remove min node in the heap
# O(log n)
def extract_min(self):
    if len(self.heap) == 0: return None
    minval = self.heap[0]
    self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
    self.heap.pop()
    self._shift_down(0)
    
    return minval


# Update value of a node
def insert_by_index(self, i, val):
    pass


def insert(self):
    pass