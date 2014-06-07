def search(A,start,end,key):
  if start>end:
    return -1
  if start == end:
    if A[start]==key:
      return start
    else:
      return -1
  mid = (start+end)/2
  if A[mid]!='':
    if key==A[mid]:
      return mid
    if key>A[mid]:
      search(A,mid+1,end,key)
    else:
      search(A,start,mid-1,key)
  else:
    right = mid+1
    while right<end and A[right]=='':
      right +=1
    if A[right] == key:
      return right
    else:
      if right==end:
        return search(A,start,mid-1,key)
      if A[right]<key:
        return search(A,right+1,end,key)
      else:
        return search(A,start,right-1,key)
      
      
  
