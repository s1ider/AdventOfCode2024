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

def compact_files(data):
	""" Compact files by moving whole files to leftmost free space blocks.
	    Move files in order of decreasing file ID. """
	# Get the maximum file ID
	max_fid = max(fid for fid in data if fid != -1)
	
	# Try to move each file, starting from the highest ID
	for fid in range(max_fid, -1, -1):
		# Find all positions of this file
		file_positions = [i for i, val in enumerate(data) if val == fid]
		
		if not file_positions:
			continue
		
		file_size = len(file_positions)
		file_start = file_positions[0]
		
		# Find the leftmost span of free space that can fit this file
		# and is to the left of the file's current position
		best_free_start = None
		i = 0
		while i < file_start:
			if data[i] == -1:
				# Found start of free space
				free_count = 0
				free_start = i
				while i < len(data) and data[i] == -1:
					free_count += 1
					i += 1
				
				# Check if this free space is large enough and before the file
				if free_count >= file_size and free_start < file_start:
					best_free_start = free_start
					break
			else:
				i += 1
		
		# If we found a suitable free space, move the file
		if best_free_start is not None:
			# Move file blocks to the free space
			for j in range(file_size):
				data[best_free_start + j] = fid
				data[file_start + j] = -1
	
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
	compacted = compact_files(unpacked)
	print(f"Compacted: {to_str(compacted)}")
	print("Checksum:", calculate_checksum(compacted))

if __name__ == '__main__':
	main()