test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def read_input(fpath=None):
	if fpath is None:
		input_text = test_input[1:]
	else:
		with open(fpath) as f:
			input_text = f.read()

	return [[int(n) for n in line.split(' ')] for line in input_text.splitlines()]

def get_order(number, next_number):
	if next_number > number:
		order = 'inc'
	if next_number < number: 
		order = 'dec'
	if next_number == number:
		order = 'eq'
	return order

def is_safe(number:int, next_number: int, order: str):
	new_order = get_order(number, next_number)
	return abs(number - next_number) < 4 and new_order != 'eq' and new_order == order


def main():
	result = []
	for report in read_input('input.txt'):
		safe = []
		for i, level in enumerate(report[:-1]):
			next_level = report[i + 1]
			order = get_order(level, next_level)
			if i > 0:
				order = get_order(report[i - 1], level)
			print(level, next_level, order)
			safe.append(is_safe(level, next_level, order))
		result.append(all(safe))
	# print(result)
	print(sum([int(r) for r in result]))

if __name__ == '__main__':
	main()