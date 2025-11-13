test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

transposition_matrix = {
	"up": 		(-1, 0),
	"down": 	(1, 0),
	"right": 	(0, 1),
	"left": 	(0, -1),
	"upright":	(-1, 1),
	"downright":(1, 1),
	"upleft": 	(-1, -1), 
	"downleft": (1, -1),
}

def read_input(fpath=None):
	if fpath is None:
		data = test_input
	else:
		with open(fpath) as f:
			data = f.read()
	lines = data.splitlines()
	return lines


def get_xx(data):
	xx = []
	print(data)
	for x, line in enumerate(data):
		for y, char in enumerate(line):
			if char == 'X':
				print(f"X: {x}, {y}")
				xx.append((x, y))
	return xx

def get_word(coord, direction, data):
	x, y = coord
	print(x, y)
	delta_x, delta_y = direction
	letters = [data[x][y]]
	for i in range(1, 4):
		if x+delta_x*i < 0 or y+delta_y*i < 0 or x+delta_x*i>=len(data) or y+delta_y*i>=len(data[x]):
			return None
		letter = data[x+delta_x*i][y+delta_y*i] 
		print(f"{letter=}")
		letters.append(letter)
	print(letters)
	return "".join(letters)

def count_xmas(x, y, data):
	count = 0
	for dir_name, direction in transposition_matrix.items():
		print(f"{dir_name=}")
		delta_x, delta_y = direction
		word = get_word((x, y), direction, data)
		print(f"{word=}")
		if word == "XMAS":
			print(f"FOUND : {x} {y} {dir_name}")
			count += 1
	return count


def main():
	data = read_input("input.txt")
	# data = read_input()
	count = 0
	xx = get_xx(data)
	print(xx)
	for x, y in xx:
		count += count_xmas(x, y, data)

	print(count)


if __name__ == '__main__':
	main()