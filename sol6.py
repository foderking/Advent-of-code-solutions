import itertools, functools

groups  = open('in').read().split('\n\n')
count = []

for i in groups:
	j = i.split()
	count.append(len(functools.reduce(lambda x, y: set(x) & set(y), j )))

print(list(itertools.accumulate(count)))