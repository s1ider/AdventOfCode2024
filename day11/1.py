def transform_stone(num):
	"""Apply transformation rules to a single stone."""
	if num == 0:
		return [1]
	
	num_str = str(num)
	if len(num_str) % 2 == 0:
		# Even number of digits - split in half
		mid = len(num_str) // 2
		left = int(num_str[:mid])
		right = int(num_str[mid:])
		return [left, right]
	
	# Odd number of digits - multiply by 2024
	return [num * 2024]

def count_stones_optimized(stones, num_blinks, memo=None):
	"""Count total stones after blinks using memoization."""
	if memo is None:
		memo = {}
	
	def count_from_stone(num, blinks_left):
		"""Recursively count stones produced from a single stone."""
		if blinks_left == 0:
			return 1
		
		if (num, blinks_left) in memo:
			return memo[(num, blinks_left)]
		
		result = sum(count_from_stone(n, blinks_left - 1) for n in transform_stone(num))
		memo[(num, blinks_left)] = result
		return result
	
	total = sum(count_from_stone(stone, num_blinks) for stone in stones)
	return total

def blink(stones):
	"""Apply one blink transformation to all stones (for display only)."""
	result = []
	for stone in stones:
		result.extend(transform_stone(stone))
	return result

def main():
	# Test with the example
	test_stones = [125, 17]
	print("Test input: 125 17")
	result = test_stones[:]
	for i in range(1, 7):
		result = blink(result)
		print(f"After {i} blink{'s' if i != 1 else ''}: {' '.join(map(str, result))}")
	
	# Part 1: 25 blinks with test input
	test_result = count_stones_optimized([125, 17], 25)
	print(f"\nTest - After 25 blinks: {test_result} stones (expected 55312)")
	
	# Read actual puzzle input
	with open('day11/input.txt') as f:
		puzzle_input = list(map(int, f.read().strip().split()))
	
	print(f"\nPuzzle input: {puzzle_input}")
	
	# Part 1: 25 blinks
	result_part1 = count_stones_optimized(puzzle_input, 25)
	print(f"Part 1 - Stones after 25 blinks: {result_part1}")
	
	# Part 2: 75 blinks
	result_part2 = count_stones_optimized(puzzle_input, 75)
	print(f"Part 2 - Stones after 75 blinks: {result_part2}")

if __name__ == '__main__':
	main()

if __name__ == '__main__':
	main()
