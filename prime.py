class prime():
  def __init__(self,range):
    self.low = pow(2,(range-1))
    self.high = pow(2,range)

  def rand(self):
    import random
    return random.randint(self.low,self.high)

  def get_prime(self):
    while True:
      a = self.rand()
      if check_prime2(a):
        return a
        break

def check_prime(n):
  if n > 1:
    for i in range(2,n):
      if (n%i)== 0:
        return False
    return True
  else:
    return False
  
def check_prime2(num):
  import random, math
  if num % 2 == 0 or num < 2:
    return False
  if num == 3:
    return True
  s = num - 1
  t = 0
  while s % 2 == 0:  # keeps halving s until it is odd
    s = s // 2
    t += 1
    for trial in range(5):
      a = random.randrange(2, num - 1)
      v = pow(a, s, num) # a is the base, s is the exponent, num is the number used for modulus
      if v != 1: # test dos not apply is v is 1
        i = 0
        while v != (num - 1):
          if i == t - 1:
            return False
          else:
            i = i+1
            v=(v**2) % num
  return True