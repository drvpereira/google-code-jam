
for case in range(1, int(input().strip()) + 1):
	s, k = input().strip().split()
	s, k = [ c == '+' for c in s], int(k)

	flips = 0
	for i in range(len(s) - k + 1):
		if not s[i]:
			s[i:i+k] = [ not p for p in s[i:i+k]]
			flips += 1

	print('Case #{0}: {1}'.format(case, flips if sum(s) == len(s) else 'IMPOSSIBLE'))