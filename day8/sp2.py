test_input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def read_input(fname=None):
	if fname is None:
		data = test_input[1:]
	else:
		with open(fname) as f:
			data = f.read()

	data = data.splitlines()
	data = [list(d) for d in data]

	return data


def scan(target_x, target_y, freq, data):
	coords = []
	for x, line in enumerate(data):
		for y, ch in enumerate(line):
			if ch == freq or ch == '#' :
				if x == target_x and y == target_y:
					continue
				coords.append((x, y))
	return coords


def get_antinode(x1, y1, x2, y2, data):
	# continue until edge

	x = x1 - (x1 - x2) * 2
	y = y1 - (y1 - y2) * 2

	x2 = x
	y2 = y

	if 0 <= x < len(data) and 0 <= y < len(data):
		print(x, y)

		coords = get_antinode(x1, y1, x, y, data)
		if coords:
			return 
		return (x, y)


def main():
	# data = read_input('input.txt')
	data = read_input()
	print(data)

	antinodes = []
	for x, line in enumerate(data):
		for y, freq in enumerate(line):
			if freq == '.':
				continue

			antennas = scan(x, y, freq, data)
			print(f"{freq=}: {antennas=}, {x=}, {y=}")
			for x2, y2 in antennas:
				antinode = get_antinode(x, y, x2, y2, data)
				if antinode:
					antinodes.append(antinode)
				# print(freq, x2, y2)
				# print(antinode)


	# update data & scan again
	for x, y in antinodes:
		data[x][y] = '#'

	for line in data:
		print("".join(line))

	antinodes = set()
	for x, line in enumerate(data):
		for y, freq in enumerate(line):
			if freq == '.' or freq == '#':
				continue

			antennas = scan(x, y, freq, data)
			print(f"{freq=}: {antennas=}, {x=}, {y=}")
			for x2, y2 in antennas:
				antinode = get_antinode(x, y, x2, y2, data)
				if antinode:
					antinodes.add(antinode)


	# one more time 
	for x, y in antinodes:
		data[x][y] = '#'

	for line in data:
		print("".join(line))


	antinodes = set()
	for x, line in enumerate(data):
		for y, freq in enumerate(line):
			if freq == '.' or freq == '#':
				continue

			antennas = scan(x, y, freq, data)
			print(f"{freq=}: {antennas=}, {x=}, {y=}")
			for x2, y2 in antennas:
				antinode = get_antinode(x, y, x2, y2, data)
				if antinode:
					antinodes.add(antinode)

	for x, y in antinodes:
		data[x][y] = '#'

	for line in data:
		print("".join(line))


	for x, line in enumerate(data):
		for y, freq in enumerate(line):
			if freq == '.':
				continue

			antennas = scan(x, y, freq, data)
			print(f"{freq=}: {antennas=}, {x=}, {y=}")
			for x2, y2 in antennas:
				antinode = get_antinode(x, y, x2, y2, data)
				if antinode:
					antinodes.add(antinode)
	

	# print(f"{antinodes=}")
	print(len(set(antinodes)))

if __name__ == '__main__':
	main()