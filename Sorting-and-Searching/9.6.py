def search(mat,elem,M,N):
  row = 0
  col = N-1
  while (row < M && col >= 0):
    if (mat[row][col] == elem):
      return true
    elif (mat[row][col] > elem):
      col-=1
    else:
      row+=1 
  return False 
