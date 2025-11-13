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

"""
MM MS SM SS 
SS MS SM MM 
"""

cases = (
	(	('MM', 'SS'),
		(-1, -1), (-1, 1),
		(1, -1), (1, 1)
	),
	(	('MS', 'MS'),
		(-1, -1), (1, -1),
		(1, 1), (-1, 1)
	),
	(	('SM', 'SM'),
		(-1, 1), (1, 1),
		(-1, -1), (1, -1)
	),
	(	('SS', 'MM'),
		(1, -1), (1, 1),
		(-1, -1), (-1, 1)
	),
)


transposition_matrix = {
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


def get_aa(data):
	aa = []
	print(data)
	for x, line in enumerate(data):
		for y, char in enumerate(line):
			if char == 'A':
				# print(f"A: {x}, {y}")
				aa.append((x, y))
	return aa

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

def find_x(x, y, m1, m2, s1, s2, data):
	m1_x, m1_y = m1
	m2_x, m2_y = m2
	s1_x, s1_y = s1
	s2_x, s2_y = s2


	m1 = x + m1_x, y + m1_y
	m2 = x + m2_x, y + m2_y
	s1 = x + s1_x, y + s1_y
	s2 = x + s2_x, y + s2_y

	for _x, _y in (m1, m2, s1, s2):
		if _x < 0 or _x >= len(data):
			print("wrong _x")
			return 0
		if _y < 0 or _y >= len(data[_x]):
			print("wrong _y")
			return 0

	for letter, c1, c2 in (('M', m1, m2), ('S', s1, s2)):
		x1, y1 = c1
		x2, y2 = c2
		if data[x1][y1] != letter and data[x2][y2] != letter:
			print(f'not X: {data[x1][y1]} != {letter}')
			return 0

	print(f'FOUND X at {x, y}')
	return 1


def count_xmas(x, y, data):
	count = 0
	print(f"{x=}, {y=}")
	for case, m1, m2, s1, s2 in cases:
		not_found = False
		# print(case)
		m1_x, m1_y = m1
		m2_x, m2_y = m2
		s1_x, s1_y = s1
		s2_x, s2_y = s2


		m1 = x + m1_x, y + m1_y
		m2 = x + m2_x, y + m2_y
		s1 = x + s1_x, y + s1_y
		s2 = x + s2_x, y + s2_y

		for _x, _y in (m1, m2, s1, s2):
			if _x < 0 or _x >= len(data):
				# print("wrong _x")
				return 0
			if _y < 0 or _y >= len(data[_x]):
				# print("wrong _y")
				return 0

		for letter, c1, c2 in (('M', m1, m2), ('S', s1, s2)):
			x1, y1 = c1
			x2, y2 = c2
			if data[x1][y1] != letter or data[x2][y2] != letter:
				# print(f'not X: {data[x1][y1]} != {letter}')
				not_found = True
				break

		if not_found:
			continue

		print(f'FOUND X at {x, y}')
		return 1

	return count


def main():
	data = read_input("input.txt")
	# data = read_input()
	count = 0
	aa = get_aa(data)
	print(aa)
	for x, y in aa:
		count += count_xmas(x, y, data)

	print(f"TOTAL COUNT: {count}")


if __name__ == '__main__':
	main()