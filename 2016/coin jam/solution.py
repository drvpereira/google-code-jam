from random import randrange
from math import floor, sqrt

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

def probably_prime(n, k):
    """
    Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.
    """
    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def find_divisors(n):
	for i in range(2,10000):
		if n % i == 0:
			return i
	return -1

def convert_to_base(n, base):
	exp = 0
	total = 0
	for digit in reversed(n):
		total += digit * pow(base, exp)
		exp += 1
	return total

def generate(jamcoin, n, solutions):
	if len(jamcoin) == n:
		solutions.append(jamcoin)
		return

	for bit in [ '0', '1' ]:
		generate(jamcoin + bit, n, solutions)

def generate_jamcoin(n, j):
	generated, partial_solutions = [], []
	generate('', (n-2)/2, partial_solutions)
	
	for partial1 in partial_solutions:
		for partial2 in partial_solutions:
			if len(generated) == j:
				break

			solution = '1' + partial1 + partial2 + '1'
			divisors = []

			for base in range(2, 11):
				number = convert_to_base(list(map(int, solution)), base)

				if not probably_prime(number, 5):
					divisor = find_divisors(number)
					if divisor > 1:
						divisors.append(divisor)

			if len(divisors) == 9:
				generated.append( (solution, divisors) )
		else:
			continue
		break

	return generated


for i in range(int(input())):
	print('Case #' + str(i+1) + ':')
	n, j = map(int, input().strip().split())
	solutions = generate_jamcoin(n, j)
	for solution in solutions:
		print(solution[0], end=' ')
		for divisor in solution[1]:
			print(divisor, end=' ')
		print()
