import random
passlen = int(input('Enter the length of password'))
s='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()?'
p=''.join(random.sample(s,passlen))
print(p)