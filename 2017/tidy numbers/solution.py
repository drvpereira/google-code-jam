
for case in range(1, int(input().strip()) + 1):
	n = list(map(int, input().strip()))
	tidy = False

	while not tidy:
		tidy = True
		for i in range(len(n)-1):
			if  n[i] > n[i+1]:
				tidy = False
				n[i] -= 1
				n[i+1:] = [ 9 for i in range(len(n) - i - 1) ]			

	print('Case #{0}: {1}'.format(case, int(''.join(map(str, n)))))