import operator


def naivek(k):
	f = open('random.txt', 'r')

	numdict = {}

	for line in f:
		num = int(line.strip())
		numdict[num] = numdict.get(num, 0)
		numdict[num] += 1

	sorted_dict = sorted(numdict.items(), key=operator.itemgetter(1))

	for i in range(1, k + 1):
		print(sorted_dict[-i])

	f.close()