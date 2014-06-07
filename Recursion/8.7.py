def makeChange( n,  denom):
  if denom==25: 
    next_denom = 10
      
  elif denom=10:
    next_denom = 5
       
  elif  denom = 5:
    next_denom = 1
  elif  denom = 1:
    return 1

  ways = 0 
  for i in range(n/denom+1):
    ways += makeChange(n - i * denom, next_denom)
  return ways
