memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

import re

with open("input.txt") as f:
	memory = f.read()

def mul(x, y):
	return x * y

def parse_memory(memory: str):
	pattern = r'mul\(\d+\,\d+\)'

	result = re.findall(pattern, memory)
	result = [eval(ins) for ins in result]
	result = sum(result)
	return result

print(parse_memory(memory))

