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
			if ch == freq:
				if x == target_x and y == target_y:
					continue
				coords.append((x, y))
	return coords


def get_antinode(x1, y1, x2, y2, data):
	delta_x = (x1 - x2)
	delta_y = (y1 - y2)

	x = x1 - delta_x*2
	y = y1 - delta_y*2

	if 0 > x or x >= len(data) or 0 > y or y >= len(data):
		print('edge', x, y)
		return None

	return (x, y)


def main():
	data = read_input('input.txt')
	# data = read_input()
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
	# print(f"{antinodes=}")
	print(len(set(antinodes)))

if __name__ == '__main__':
	main()