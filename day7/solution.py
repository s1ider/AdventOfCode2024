test_input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
from operator import add, mul
from itertools import product


def read_input(fname=None):
	"""Read and parse input file or test input."""
	if fname is None:
		data = test_input.strip()
	else:
		with open(fname) as f:
			data = f.read().strip()

	equations = []
	for line in data.splitlines():
		target, numbers = line.split(': ')
		equations.append((int(target), [int(n) for n in numbers.split()]))
	
	return equations


def is_equation_true(numbers, expected, debug=False):
	"""Check if any combination of + and * operators can produce the expected result."""
	n_operators = len(numbers) - 1
	
	# Try all possible combinations of operators (2^n_operators combinations)
	for ops in product((add, mul), repeat=n_operators):
		result = numbers[0]
		for i, op in enumerate(ops):
			result = op(result, numbers[i + 1])
		
		if result == expected:
			if debug:
				op_symbols = ['*' if op == mul else '+' for op in ops]
				print(f"  Found: {numbers[0]} {' '.join(f'{op_symbols[i]} {numbers[i+1]}' for i in range(len(op_symbols)))} = {expected}")
			return True
	
	return False


def solve(fname='input.txt'):
	"""Solve the calibration equation problem."""
	equations = read_input(fname)
	
	print(f"Processing {len(equations)} equations...")
	
	total = sum(
		target for target, numbers in equations
		if is_equation_true(numbers, target)
	)
	
	return total


def main():
	# Test with example - debug each equation
	equations = read_input(None)
	print("Testing each example equation:")
	valid_sum = 0
	for target, numbers in equations:
		is_valid = is_equation_true(numbers, target)
		if is_valid:
			valid_sum += target
		print(f"{target}: {numbers} -> {is_valid}")
	
	print(f"\nTest result: {valid_sum} (expected: 3749)")
	
	# Solve with actual input
	result = solve('input.txt')
	print(f"Part 1 result: {result}")


if __name__ == '__main__':
	main()