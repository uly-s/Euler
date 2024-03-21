from functools import reduce

num = 2**1000

numstr = str(num)

numlist = [int(numstr[i]) for i in range(len(numstr))]

print(numlist)

sum = reduce(lambda x,y: x+y, numlist)

print(sum)