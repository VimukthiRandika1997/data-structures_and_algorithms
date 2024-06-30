'''

For Inorder -> we do something between left and right
For Preorder -> we do something before left and right
For Postorder -> we do something after left and right

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

res = []

# Visit Left, Root, Right
def inorder(root):
    if not root: return []

    inorder(root.left)
    res.append(root.val)
    inorder(root.right)

    return res


# Vist Root, Left, Right
def preorder(root):
    if not root: return []

    res.append(root.val)
    preorder(root.left)
    preorder(root.right)

    return res


# Visit Left, Right, Root
def postorder(root):
    if not root: return []
    
    postorder(root.left)
    postorder(root.right)
    res.append(root.val)

    return res


'''

Stack based approach: No recursion 

'''

    