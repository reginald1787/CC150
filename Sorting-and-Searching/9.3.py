
def BinarySearch(A,key):
  n = len(A)
  if n<=0:
    return -1
  mid = n/2
  if A[mid]==key:
    return mid
  if A[0]==key:
    return 0
  if mid+1>n-1:
    return -1
  if A[0]<A[mid]:
    if key<A[mid]:
      if key>A[0]:
        return BinarySearch(A[:mid],key)
    return mid + 1+ BinarySearch(A[mid+1:],key)
  else:
    if key>A[mid]:
      if key<A[0]:
        return mid + 1+ BinarySearch(A[mid+1:])
    return BinarySearch(A[:mid])

        
  
