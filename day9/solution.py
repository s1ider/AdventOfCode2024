test_input = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
from pprint import pprint


def read_input(fname=None):
	if fname is None:
		data = test_input[1:]
	else:
		with open(fname) as f:
			data = f.read()

	data = data.splitlines()
	data = [d.split(' ') for d in data]

	return data


def move_head(head_pos, direction, steps):
    x, y = head_pos
    if direction == 'R':
        y += steps
    elif direction == 'L':
        y -= steps
    elif direction == 'U':
        x -= steps
    elif direction == 'D':
        x += steps
    return (x, y)

def move_tail(head_pos, tail_pos, direction, steps):
	hx, hy = head_pos
	tx, ty = tail_pos

	for _ in range(steps):
		# Move head one step at a time
		if direction == 'R':
			hy += 1
		elif direction == 'L':
			hy -= 1
		elif direction == 'U':
			hx -= 1
		elif direction == 'D':
			hx += 1

		# Update tail position based on head position
		if abs(hx - tx) > 1 or abs(hy - ty) > 1:
			if hx > tx:
				tx += 1
			elif hx < tx:
				tx -= 1
			if hy > ty:
				ty += 1
			elif hy < ty:
				ty -= 1

	return (tx, ty)

def main():
	# data = read_input('input.txt')
	data = read_input()
	print(data)


if __name__ == '__main__':
	main()