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


class ReachedEnd(Exception):
	pass

def read_input(fname=None):
	if fname is None:
		input_map = map_text[1:]
	else:
		with open(fname) as f:
			input_map = f.read()

	inp = [ list(line) for line in input_map.splitlines()]
	return inp


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
	# print(f"new direction: {dir_name}")

	return direction


def move(x, y, direction, level, visited):
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
		# print("reached the end")
		visited.append((x, y))
		raise ReachedEnd


def print_level(map_s, level=None, symbol='X'):
	if level is None:
		size = 10
	else:
		size = len(level)
	level = [list('.' * size) for _ in range(size) ]
	for x, y in map_s:
		level[x][y] = symbol

	for l in level:
		print("".join(l))


	return level

def get_start_coord(level):
	start_symbol = '^'
	for x, line in enumerate(level):
		for y, ch in enumerate(line):
			if level[x][y] == start_symbol:
				return x, y

def pprint_level(level):
	for line in level:
		print("".join(line))


def detect_loop(level):
	visited = []
	iters = 0
	loop = True
	x, y = get_start_coord(level)
	direction = (-1, 0)
	while iters < 10000:
		try:
			x, y, direction = move(x, y, direction, level, visited)
			iters += 1
		except ReachedEnd:
			print("no loop")
			loop = False
			print(f"{iters=}")
			iters = 0
			return loop, len(set(visited))

	# print(f"{loop=}", f"{iters=}")
	return loop, len(set(visited))


def get_obstacles(level, symbol='#'):
	obstacles = set()
	for x, line in enumerate(level):
		for y, ch in enumerate(line):
			if level[x][y] == symbol:
				obstacles.add((x, y)) 
	return obstacles
 

def possible_insertions(level):
	size = len(level)
	coords = set([(x, y) for x in range(size) for y in range(size)])

	obstacles = get_obstacles(level, '#')

	start_x, start_y = get_start_coord(level)
	start_direction = (-1, 0)
	obstacles.add((start_x, start_y))
	obstacles.add((start_x + start_direction[0], start_y + start_direction[1]))
	
	# insertion
	# obstacles = obstacles | get_obstacles(level, 'o')

	all_possible_coords = coords.difference(obstacles) 
	return all_possible_coords


def main():
	level = read_input("input.txt")
	# level = read_input()

	start_x, start_y = get_start_coord(level)
	direction = (-1, 0)
	print(f"start: {start_x, start_y}")
	print(f"loop is {detect_loop(level)}")

	pprint_level(level)
	possibles = possible_insertions(level)
	print_level(possibles, level, 'O')

	loops = []
	for o in possibles:
		o_x, o_y = o
		# print(f"{o=}")
		level = read_input("input.txt")
		# level = read_input()
		level[o_x][o_y] = '#'
		# pprint_level(level)
		is_loop, visited_count = detect_loop(level)
		# print(is_loop, visited_count)
		if is_loop:
			print(f"DETECTED LOOP AT {o}")
			loops.append(o)
	print(len(loops))
	print(loops)

if __name__ == '__main__':
	main()