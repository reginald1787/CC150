Class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
Class LinkedList:
    def __init__(self,val):
        self.val = val
        self.left = None

        
def TreetoList(root):
    if root == None:
        return []
    list = []
    queue = [root]
    while queue!=[]:
        n = length(queue)
        currlist =  [LinkedList(node.val) for node in queue]
        for i in range(n-2,-1,-1):
            currlist[i].next = currlist[i+1]
        list.append(currlist)
        for i in range(n):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return list
