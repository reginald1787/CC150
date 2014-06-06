Class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def findnode(root,node):
    if root == node:
        return True
    if root == None or isleaf(root):
        return False
    return findnode(root.left,node) or findnode(root.right,node)
    
    

def findancestor(node1,node2,root):
    if root == None or isleft(root) :
        return None
    if findnode(root.left,node1) and findnode(root.left,node2):
        return findancestor(node1,node2,root.left)
    if findnode(root.right,node1) and findnode(root.right,node2):
        return findancestor(node1,node2,root.right)
    return root
