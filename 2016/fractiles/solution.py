def get_index(start):
	index, current = 0, start
	for i in range(c):
		index = index * k + current
		if current < k - 1:
			current += 1
	return index + 1

for case in range(1, int(input()) + 1):
	k, c, s = map(int, input().split(' '))
	
	if s * c < k:
		print('Case #{0}: IMPOSSIBLE'.format(case))
	else:
		solution = ''
		for i in range(0, k, c):
			solution += str(get_index(i)) + ' '

		print('Case #{0}: {1}'.format(case, solution))
