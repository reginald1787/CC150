Class GraphNode:
  def __init__(self,val):
      self.val = val
      self.next = None
      
      
      
def DFS(node1,node2,visited):
    if node1==node2:
        return True
    if node1==None:
        return False
    visited.add(node1)
    if node1.next not in visited:
        return DFS(node1.next,node2,visited)
    else:
        return False
    
def isRoute(node1,node2):
    visited = set([])
    return DFS(node1,node2, visited)
