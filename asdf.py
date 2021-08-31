# PART 1
f = open('in')
seats = f.read().split("\n")
no = 0 
val = []
missing = []

def bsp(tup, st):
    one = tup[0]
    two = tup[1]
    diff = int((tup[1] - tup[0] + 1) / 2)

    if st == 'F' or st == 'L':
        return (one, one + diff - 1)
    else:
        return (one + diff, two)

def no_get(st, n):
    for i in st:
        n = bsp(n, i)
    if n[1] == n[0]:
        return n[1] 
    else:
        print('Errroor')

def id_get(st):
    row = no_get( st[:-3], (0,127) )
    col = no_get( st[-3:], (0,7) )
    val.append(row * 8 + col)
    return row * 8 + col


for i in seats:
    n = id_get(i)
    if n > no:
        no = n

# PART 2
for i in range(1,127):
    for j in range(8):
        if (i * 8 + j) not in val:
            missing.append(i * 8 + j)

print(missing)