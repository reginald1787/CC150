Class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        
        
        
        
        
def findnext(node,root):
    if root and node:
        if node.right:
            mostleft = node.right
            while mostleft.left:
                mostleft = mostleft.left
            return mostleft
        else:
            if node.parent == None:
                return None
            parent = node.parent
            if parent.left == node:
                return parent
            grandparent = parent.parent
            while grandparent and grandparent.right = parent:
                parent = grandparent
                grandparent = grandparent.parent
            
            return grandparent
            
                
