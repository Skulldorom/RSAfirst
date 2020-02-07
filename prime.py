class prime():
  def __init__(self,l,h):
    self.low = l
    self.high = h

  def rand(self):
    import random
    return random.randint(self.low,self.high)

  def get_prime(self):
    a = self.rand()
    if check_prime(a):
      return a
    else:
      return self.get_prime()

def check_prime(n):
  if n > 1:
    for i in range(2,n):
      if (n%i)== 0:
        return False
    return True
  else:
    return False
  
