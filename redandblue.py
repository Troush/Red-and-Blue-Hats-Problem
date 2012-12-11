import random

color = ['red','blue']

def colorize(color):
	if color == 'red':
		return 0
	else: return 1
def uncolorize(color):
	if color == 1:
		return 'red'
	else: return 'blue'
def logical_xor(str1, str2):
    return colorize(str1) ^ colorize(str2)


def first(array):
	answers = {}
	for el in array:
		if el == 0:
			answers[0] = array[el+1]
		answers[el] = uncolorize(logical_xor(array.get(el-1),array.get(el+1)))
	return answers
randb = {}
ppl = {}
for men in range(100):
	c = random.randrange(0,2)
	randb[men] = color[c]
for men in randb:
	print str(men) + " " + randb.get(men)
answer = first(randb)
count = 0
for qv in range(100):
	if randb.get(qv) == answer.get(qv):
		count += 1
print count