
def map_t9(c):
	if c == ' ':
		key = '0'
		qty = 1
	elif c in 'abc':
		key = '2'
		qty = 1 + ((ord(c) - 97) % 3)
	elif c in 'def':
		key = '3'
		qty = 1 + ((ord(c) - 97) % 3)
	elif c in 'ghi':
		key = '4'
		qty = 1 + ((ord(c) - 97) % 3)
	elif c in 'jkl':
		key = '5'
		qty = 1 + ((ord(c) - 97) % 3)
	elif c in 'mno':
		key = '6'
		qty = 1 + ((ord(c) - 97) % 3)
	elif c in 'pqrs':
		key = '7'
		qty = 1 + ((ord(c) - 112) % 4)
	elif c in 'tuv':
		key = '8'
		qty = 1 + ((ord(c) - 116) % 3)
	else:
		key = '9'
		qty = 1 + ((ord(c) - 119) % 4)
	
	return (key, qty)

for n in range(int(input())):
	old_key = ''
	result = ''
	for c in input():
		key, qty = map_t9(c)
		if key == old_key:
			result += ' '
		result += key * qty
		old_key = key

	print("Case #{}: {}".format(n+1, result))