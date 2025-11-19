test_input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

def read_input(fname=None):
	if fname is None:
		data = test_input[1:]
	else:
		with open(fname) as f:
			data = f.read()
	data = [[int(ch) for ch in data_line.strip()] for data_line in data.strip().splitlines()]
	return data


def get_trailheads(data):
	for y, row in enumerate(data):
		for x, num in enumerate(row):
			if num == 0:
				yield (x, y)


def get_next_steps(data, x, y) -> list[tuple[int, int]]:
	width = len(data[0])
	height = len(data)
	directions = [(-1,0), (1,0), (0,-1), (0,1)]  # left, right, up, down

	cur_num = data[y][x]
	next_num = cur_num + 1
	next_steps = []
	for dx, dy in directions:
		nx, ny = x + dx, y + dy
		if 0 <= nx < width and 0 <= ny < height and data[ny][nx] == next_num:
			next_steps.append((nx, ny))

	return next_steps

def explore_trail(data, x, y, top_reached):
	if data[y][x] == 9:
		top_reached.add((x, y))
		return
	
	for nx, ny in get_next_steps(data, x, y):
		explore_trail(data, nx, ny, top_reached)

def get_trail_score(data, x, y):
	top_reached = set()
	explore_trail(data, x, y, top_reached)
	return len(top_reached)


def main():
	data = read_input('day10/input.txt')
	# data = read_input()
	trailheads = list(get_trailheads(data))
	print(f"Trailheads = {len(trailheads)} {trailheads}")
	scores = [get_trail_score(data, trail[0], trail[1]) for trail in trailheads]
	# print(f"Scores = {scores}")
	print(f"Total score = {sum(scores)}")
	

if __name__ == '__main__':
	main()