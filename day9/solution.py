test_input = """
2333133121414131402
"""

def read_input(fname=None):
	if fname is None:
		data = test_input[1:]
	else:
		with open(fname) as f:
			data = f.read()

	return data.strip()

def unpack(data):
	unpacked_data = []
	for fid, i in enumerate(range(0, len(data), 2)):
		fill = int(data[i])
		free = int(data[i+1]) if i+1 < len(data) else 0
		unpacked_data.extend([fid] * fill)  # Use fid as int, not string
		unpacked_data.extend([-1] * free)   # Use -1 for free space instead of '.'
	return unpacked_data


def calculate_checksum(data):
	checksum = 0
	for i, ch in enumerate(data):
		if ch != -1:
			checksum += ch * i
	return checksum


def get_next_free(data):
	for i, ch in enumerate(data):
		if ch == -1:
			return i
	return -1

def free_space(data):
	""" defragment data - optimized with two pointers """
	left = 0  # Pointer for next free space
	right = len(data) - 1  # Pointer for next file block
	
	while left < right:
		# Find next free space from left
		while left < len(data) and data[left] != -1:
			left += 1
		
		# Find next file block from right
		while right >= 0 and data[right] == -1:
			right -= 1
		
		# Stop if pointers crossed
		if left >= right:
			break
		
		# Swap file block with free space
		data[left], data[right] = data[right], data[left]
		left += 1
		right -= 1
	
	return data

def to_str(data):
	result = []
	for ch in data:
		if ch == -1:
			result.append('.')
		else:
			result.append(str(ch))
	return ''.join(result)

def main():
	data = read_input('day9/input.txt')
	# data = read_input()
	unpacked = unpack(data)
	print(f"Unpacked: {to_str(unpacked)}")
	defragmented = free_space(unpacked)
	print(f"Defragmented: {to_str(defragmented)}")
	print("Checksum:", calculate_checksum(defragmented))

if __name__ == '__main__':
	main()