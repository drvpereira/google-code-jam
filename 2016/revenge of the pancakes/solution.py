
for case in range(int(input())):
	pile = list(input())
	current = pile[0]
	flips = 0

	for pancake in pile:
		if pancake != current:
			flips += 1
		current = pancake

	if pancake[-1] == '-':
		flips += 1

	print('Case #' + str(case+1) + ': ' + str(flips))