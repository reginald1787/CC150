

def sort(A):
  Ht = sorted(A) # [(3,1),(1,9),(2,2)] would be [(1,9),(2,2),(3,1)]
  num = len(Ht)
  pre_wt = Ht[num-1][1]
  unfit = 0
  for i in range(num-2,-1,-1):
    if Ht[i][1]>pre_wt or Ht[i][0]==Ht[i+1][0]:
      unfit+=1
    pre_wt=Ht[i][1]
    
  return num-unfit
    
  
  
