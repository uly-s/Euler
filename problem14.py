# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

def collatz(n):
    return n//2 if n % 2 == 0 else (3*n)+1

n = 13
for i in range(13, 23):
    #print(collatz(n))
    n = collatz(n) 

# searching for the max length of a collatz sequence
# from starting number to 1, what starting number
# (under a million) has the biggest length?
    
# first, function to get the length of a collatz seq
# from a starting number
    
def collatzseqlen(n):
    x = n
    count = 1
    while x != 1:
        count += 1
        x = collatz(x)
    return count


# max len
maxlen = 0

# max start
maxstart = 0

# starting from 13, going to 1 million
for i in range(13, 1000000):
    seqlen = collatzseqlen(i)
    if (seqlen > maxlen):
        maxlen = seqlen
        maxstart = i
        print(maxstart, maxlen)

print(i)
