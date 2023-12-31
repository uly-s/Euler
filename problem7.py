# write a function to find the 10001st prime number
def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def prime10001():
    count = 0
    for i in range(2, 1000000000):
        if prime(i):
            count += 1
            if count == 10001:
                return i
            
print(prime10001())