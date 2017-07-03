def find_items(prices, c):
	for i1, p1 in enumerate(prices):
		for i2, p2 in enumerate(prices):
			if p1 + p2 == c and i1 != i2:
				return (i1+1, i2+1)
	return None
	

for n in range(int(input())):
	c, i = int(input()), int(input())
	prices = list(map(int, input().split()))

	result = find_items(prices, c)
	if result:
		print("Case #{}: {} {}".format(n+1, result[0], result[1]))