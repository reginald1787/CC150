

def setbit(N,M,i,j):
    max = ~0
    left = max - ((1<<j) -1)
    right = (1<<i)-1
    mask = left|right
    return (N&mask) | (M<<i)
    
