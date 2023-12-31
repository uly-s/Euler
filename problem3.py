num = 600851475143

def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def factor(x,y):
    if x % y == 0:
        return True
    return False

max = 0

for i in range(1, num):
    if prime(i) and factor(num, i):
        max = i
        print(max)

print(max)