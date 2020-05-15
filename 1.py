import random
m = int(input('Unesi m \n'))
n = int(input('Unesi n \n'))
k = int (input('Unesi k \n'))
br = 0
a = random.randint(m,n)
while br is 0:
    if a%k is 0:
        print(a)
        br = 1
    else:
        a = random.randint(m,n)