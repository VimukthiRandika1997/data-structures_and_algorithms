# TreeNode
class TreeNode:
    def __init_(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def search(root, target):
    if not root: # checking whehter root is null or not
        return False

    if target > root.val:
        return search(root.right, target) 
    elif target < root.val:
        return search(root.left, target)
    else:
        return True