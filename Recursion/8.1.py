
def Fibonacci(n):
  if n<2:
    return n
  if n%2==0:
    m = n/2
    return Fibonacci(m)**2+2*Fibonacci(m-1)*Fibonacci(m)
  else:
    m = (n+1)/2
    return Fibonacci(m)**2+Fibonacci(m-1)**2
