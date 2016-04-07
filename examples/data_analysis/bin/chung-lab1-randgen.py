import numpy as np

randnumfile = open("random.txt", "w")
i = 0
N = 10000000

while i <= N:
	num = np.random.randint(0, 3)
	if num == 2:
		line = str(np.random.randint(2, 10000**2))
		randnumfile.write(line + "\n")
		i += 1
	else:
		line = str(num)
		randnumfile.write(line + "\n")
		i += 1

randnumfile.close()