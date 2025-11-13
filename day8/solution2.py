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


def get_all_antennas_by_freq(data):
	"""Group all antennas by their frequency"""
	freq_map = {}
	for x, line in enumerate(data):
		for y, ch in enumerate(line):
			if ch != '.':
				if ch not in freq_map:
					freq_map[ch] = []
				freq_map[ch].append((x, y))
	return freq_map


def get_antinodes_for_pair(x1, y1, x2, y2, data):
	"""Get all antinodes on the line passing through two antennas"""
	antinodes = set()
	
	# Calculate the direction vector
	delta_x = x2 - x1
	delta_y = y2 - y1
	
	# Find GCD to get the smallest step direction
	from math import gcd
	g = gcd(abs(delta_x), abs(delta_y))
	step_x = delta_x // g
	step_y = delta_y // g
	
	# Walk in both directions from x1
	x, y = x1, y1
	height = len(data)
	width = len(data[0]) if data else 0
	
	while 0 <= x < height and 0 <= y < width:
		antinodes.add((x, y))
		x += step_x
		y += step_y
	
	# Walk in the opposite direction from x1
	x, y = x1 - step_x, y1 - step_y
	while 0 <= x < height and 0 <= y < width:
		antinodes.add((x, y))
		x -= step_x
		y -= step_y
	
	return antinodes


def main():
	data = read_input('input.txt')
	# data = read_input()

	antinodes = set()
	freq_map = get_all_antennas_by_freq(data)
	
	# For each frequency, find all antinodes
	for freq, positions in freq_map.items():
		# Need at least 2 antennas to create antinodes
		if len(positions) < 2:
			continue
		
		# For each pair of antennas with the same frequency
		for i in range(len(positions)):
			for j in range(i + 1, len(positions)):
				x1, y1 = positions[i]
				x2, y2 = positions[j]
				
				# Get all antinodes on the line between these two antennas
				pair_antinodes = get_antinodes_for_pair(x1, y1, x2, y2, data)
				antinodes.update(pair_antinodes)
	
	print(f"Total antinodes: {len(antinodes)}")


def visualize(data, antinodes):
	"""Print the map with antinodes marked"""
	height = len(data)
	width = len(data[0])
	
	for x in range(height):
		row = []
		for y in range(width):
			if (x, y) in antinodes:
				row.append('#')
			else:
				row.append(data[x][y])
		print(''.join(row))


if __name__ == '__main__':
	main()
