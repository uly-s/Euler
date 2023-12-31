min = 0

def divisible1to20(x):
    for i in range(1, 21):
        if x % i != 0:
            return False
    return True

for i in range(1, 1000000000):

    divisible = divisible1to20(i)

    if divisible:
        print(i)
        min = i
        break

print(min)