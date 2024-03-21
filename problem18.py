tree_str = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

lines = tree_str.split("\n");
lines.pop(0)
rows = [lines[i].split(" ") for i in range(len(lines))]
#print(rows)


tree = [[] for i in range(15)]

counter = 1
sum = 0 

for i in range(15):
    for j in range(counter):
        tree[i].append(int(rows[i][j]))
    counter += 1
    sum += counter

# for i in range(15):
#     print(tree[i])

size=15
counter = 0
sum = 0
flip = 0
meta = 0

for count in range(size):
    sum = 0
    for i in range(15):
        for j in range(counter, counter+1):
            if i == 1 and j == 1:
                sum += tree[i][j]
            else:
                if count > 0:
                    if i != size-count:
                        sum += tree[i][j]
                    else:
                        meta += 1
                        sum += tree[i][j+1]
                else:
                    sum += tree[i][j]

    print(sum)
    flip = 15

print(meta)

def iter(n):
  """Iterates over all binary strings of length n."""
  for i in range(2**n):
    binary_string = format(i, '0{}b'.format(n))
    yield binary_string

# so let's just say
max = 0
    
for path in iter(size):
    sum = 0
    j = 0
    sum += tree[0][0]
    for i in range(1, size):
        if path[i] == '0':
            # go left
            sum += tree[i][j]
        else:
            # go right
            j += 1
            sum += tree[i][j]

    if sum > max:
        max = sum

print(max)

# let's also just say 
