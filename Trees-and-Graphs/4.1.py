Class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    

def isleaf(node):
    if node.left==None and node.right==None:
        return True
    else:
        return False
    
def maxdst(root):
    if root == None or isleaf(root):
        return 0
    return max(maxdst(root.left),maxdst(root.right)+1
    
def mindst(root):
    if root == None: 
        return 999999
    if isleaf(root):
        return 0
    
    return min(mindst(root.left),mindst(root.right)+1
    
def isBalanced(root):
    if root == None or isleaf(root):
        return True
    if maxdst(root) - mindst(root) >1:
        return False
    return True
    
