memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

import re

with open("input.txt") as f:
	memory = f.read()

pattern_do = r'do\(\)'
pattern_dont = r"don't\(\)"
pattern = r'mul\(\d+\,\d+\)'


def mul(x, y):
	return x * y


def find_next_dont(memory):
	match = re.search(pattern_dont, memory)
	index = match.end() if match else len(memory)
	print(f"dont: {index}")
	return index


def find_next_do(memory):
	match = re.search(pattern_do, memory)
	index = match.end() if match else len(memory)
	print(f"do: {index}")
	return index


def get_memory_chunk(do_ind:int, dont_ind:int):
	if dont_ind < do_ind:
		return memory[dont_ind:do_ind]
	else:
		return memory[do_ind:dont_ind]


def parse_memory(memory: str):
	do_flag = True
	result = []
	cur_index = 0
	memory_chunk = memory
	while memory_chunk:
		# print(f"chunk: {memory_chunk[:1000]}")
		next_do = find_next_do(memory_chunk)
		next_dont = find_next_dont(memory_chunk)

		next_ind = min(next_do, next_dont)
		if cur_index > len(memory) - next_ind:
			next_ind = len(memory)
		memory_evals = memory_chunk[:next_ind]

		print(f"{cur_index=}")
		print(f"{do_flag=}")
		print(f"{memory_chunk[:1000]}")
		print(f"{next_ind=}")

		if do_flag:
			instructions = re.findall(pattern, memory_evals)
			print(instructions)
			instructions = [eval(ins) for ins in instructions]
			result.append(sum(instructions))

		memory_chunk = memory_chunk[next_ind:]
		do_flag = next_do <= next_dont
		cur_index = next_ind

	return result

r = parse_memory(memory)
print(r)
print(sum(r))

