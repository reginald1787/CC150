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
        
        
def matchtree(root1,root2):
    if root1 == None and root2 ==None:
        return True
    elif root1 and root2 == None:
        return False
    elif root2 and root1 == None:
        return False
    if root1.val == root2.val:
        if matchtree(root1.left,root2.left) and matchtree(root1.right,root2.right):
            return True
            
    return False
    
def subtree(T1,T2):
    queue = [T1]
    matched = False
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop(0)
            matched = matchtree(node,T2)
            if matched:
                return matched
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return matched
