from prime import prime

def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b)

class RSA():
  def __init__(self, keylength):
    self.range = keylength
    self.n,self.e,self.d,self.p,self.q,self.t = self.calc()

  def calc(self):
    while True:
      p = prime(self.range).get_prime()
      q = prime(self.range).get_prime()
      if p != q:
        break

    n = p * q
    t = (p-1)*(q-1)

    for e in range(2,t): 
      if gcd(e,t)== 1: 
        break

    for i in range(1,10): 
        x = 1 + i*t 
        if x % e == 0: 
            d = x//e
            if d != e: 
              break

    return n,e,d,p,q,t

  def print_vars(self):
    print('p:',self.p)
    print('q:',self.q)    
    print('n:',self.n)
    print('t:',self.t)
    print('e:',self.e)
    print('d:',self.d)
    
  def get_private(self):
    print ('private is: (',self.d,',',self.n,')')
  
  def get_public(self):
    print ('public is: (',self.e,',',self.n,')')

  def encrypt(self,text):
    return pow(text,self.e,self.n)

  def decrypt(self,text):    
    return pow(text,self.d,self.n)

def string_to_number(text):
  pass

def number_to_string(numebr):
  pass