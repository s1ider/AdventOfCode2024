test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def read_input(fpath=None):
    if fpath is None:
        input_text = test_input[1:]
    else:
        with open(fpath) as f:
            input_text = f.read()

    return [[int(n) for n in line.split(' ')] for line in input_text.splitlines()]

def get_order(number, next_number):
    if next_number > number:
        order = 'inc'
    if next_number < number: 
        order = 'dec'
    if next_number == number:
        order = 'eq'
    return order

def is_safe_level(level:int, next_level: int, order: str):
    new_order = get_order(level, next_level)
    safe = abs(level - next_level) < 4 and new_order != 'eq' and new_order == order

    return safe

def report_safe_details(report):
    safe = []

    for i, level in enumerate(report[:-1]):
        next_level = report[i + 1]
        order = get_order(level, next_level)
        if i > 0:
            order = get_order(report[i - 1], level)
        # print(level, next_level, order)
        safe.append(is_safe_level(level, next_level, order))

    return safe


def main():
    result = []
    fpath = 'input.txt'
    # fpath = None
    for report in read_input(fpath):
        report_status_safe = report_safe_details(report)
        given_report = report.copy()
        if not all(report_status_safe):
            for ind, level in enumerate(report):
                # ind = report_status_safe.index(False)
                report = given_report.copy()
                del report[ind]
                report_status_safe = report_safe_details(report)
                if all(report_status_safe):
                    print(f"Damped: {report} from {given_report} without {given_report[ind]} at {ind+1}")    
                    break
            else:
                print(f"UNSAFE: {report} from {given_report} without {given_report[ind]} at {ind+1}")
        result.append(all(report_status_safe))
    # print(result)
    print(sum([int(r) for r in result]))

if __name__ == '__main__':
    main()