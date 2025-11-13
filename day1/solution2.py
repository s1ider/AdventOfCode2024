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
    # s1, s2 = read_input()
    result = []
    
    for line in s1:
        result.append((line, line*s2.count(line)))
    print(result)
    similarity_score = sum([r[1] for r in result])
    print(f"{similarity_score=}")



if __name__ == '__main__':
    main()
