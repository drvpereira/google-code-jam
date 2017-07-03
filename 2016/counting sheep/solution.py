from collections import Counter

for case in range(1, int(input())+1):
	n, current = int(input().strip()), 'INSOMNIA'
	
	if n != 0:
		char_count, current = Counter(str(n)), n
		while len(char_count.values()) < 10:
			current += n

			char_count += Counter(str(current))

	print('Case #{0}: {1}'.format(case, current))