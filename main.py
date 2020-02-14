from RSA import RSA

type1 = RSA(1000)
'''type1.print_vars()
type1.get_public()
type1.get_private()'''

x = type1.encrypt(5)
y = type1.decrypt(x)

print('\nencrypted is: ',x,"\ndecrypted is: ",y)
