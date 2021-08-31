import pprint, re
from itertools import accumulate

var = open('in').read()
no = []

dic = {}
direct = []
sub = []
j = var.split('\n')
for i in j :
	dic[i.split('contain')[0]] = i.split('contain')[1].strip('.')


def dir(s_t):
	# finding the direct bags
	for x, y in dic.items():
		if re.search(s_t, y):
			# direct.append(x.strip()[:-1])
			yield x.strip()[:-1]
	# finding no of indirect bags:
def redir():
	global ree
	sub = []
	for x, y in dic.items():
		for i in ree:
			if re.search(i, y):
				sub.append(x.strip()[:-1])
	print(len(set(sub)))
	no.append(len(set(sub)))
	ree = sub
	if not len(set(sub)) == 0:
		redir()


s_no = len(set(sub))

o = list(dir('shiny gold'))
ree = o
redir()
print(list(accumulate(no)))