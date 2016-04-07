import operator

f = open('random.txt'm 'r')

def naivek(k):
	numdict = {}

	for line in f:
		num = int(line.strip())
		numdict.get(num, 0)
		numdict[num] += 1

	sorted_dict = sorted(numdict.items(), key=operator.itemgetter(1))

	for i in range(k):
		print(sorted_dict[i])

naivek(2)

f.close()