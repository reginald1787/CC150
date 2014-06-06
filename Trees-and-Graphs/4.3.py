Class TreeNode:
  def __init__(self,val):
      self.val = val
      self.left = None
      self.right = None
      
      
      
def buildTree(array):
    n = len(array)
    if n==0:
        return None
    if n==1:
        node = TreeNode(array[n-1])
        return node
    mid = n/2
    root = TreeNode(array[mid])
    left = buildTree(array[:mid])
    right = buildTree(array[mid+1:])
    root.left = left
    root.right = right
    return root
