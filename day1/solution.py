test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

def read_input(fpath=None):
    if fpath is None:
        pairs_text = test_input[1:]
    else:
        with open(fpath) as f:
            pairs_text = f.read()
    pairs = [line.split('   ') for line in pairs_text.splitlines()]
    set1 = [int(p[0]) for p in pairs]
    set2 = [int(p[1]) for p in pairs]

    return set1, set2

def main():
    # get lists of numbers

    s1, s2 = read_input("input.txt")
    s1, s2 = read_input()
    result = []
    # calc smallest for each + distance
    for line in range(len(s1)):
        next_min_1 = min(s1)
        s1.remove(next_min_1)
        next_min_2 = min(s2)
        s2.remove(next_min_2)
        distance = abs(next_min_1 - next_min_2)

        result.append((next_min_1, next_min_2, distance))
    print(result)
    # calc total distance
    total_distance = sum([r[2] for r in result])
    print(f"{total_distance=}")



if __name__ == '__main__':
    main()
