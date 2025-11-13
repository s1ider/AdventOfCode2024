map_text = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

directions = {
		'n': (-1, 0),
		's': (1, 0),
		'e': (0, 1),
		'w': (0, -1),
}

visited = []


def read_input(fname=None):
	if fname is None:
		input_map = map_text[1:]
	else:
		with open(fname) as f:
			input_map = f.read()

	return input_map.splitlines()


def turn_right(direction):
	turn_map = {
		(-1, 0): (1, 1),
		(1, 0): (-1, -1),
		(0, 1): (1, -1),
		(0, -1): (-1, 1)
	}
	x, y = direction
	delta_x, delta_y = turn_map[direction]
	direction = x + delta_x, y + delta_y
	dir_name = {v: k for k, v in directions.items()}[direction]
	print(f"new direction: {dir_name}")

	return direction


def move(x, y, direction, level):
	delta_x, delta_y = direction
	new_x, new_y =	x, y
	if 0 <= x+delta_x < len(level) and 0 <= y+delta_y < len(level[x]):
		new_x, new_y = x + delta_x, y + delta_y
		# print(new_x, new_y)

		if level[new_x][new_y] == '#':
			# turn direction to 90 right
			direction = turn_right(direction)
			new_x, new_y = x, y
		else:
			# store current cell as visited
			visited.append((x, y))
		# print(new_x, new_y, direction)
		return new_x, new_y, direction
	else:
		print("reached the end")
		visited.append((x, y))
		raise StopIteration


def print_level(map_s, level=None, symbol='X'):
	if level is None:
		size = 10
	else:
		size = len(level)
	level = [list('.' * size) for _ in range(size) ]
	for x, y in map_s:
		level[x][y] = 'X'

	for l in level:
		print("".join(l))

	return level

def get_start_coord(level):
	start_symbol = '^'
	for x, line in enumerate(level):
		for y, ch in enumerate(line):
			if level[x][y] == start_symbol:
				return x, y

def main():
	# move
	level = read_input("input.txt")
	# level = read_input()
	x, y = get_start_coord(level)
	direction = (-1, 0)
	while 1:
		try:
			x, y, direction = move(x, y, direction, level)
		except StopIteration:
			break

	print(len(set(visited)))
	print_level(visited, level)

if __name__ == '__main__':
	main()