test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def is_valid(number, update, rules):
	for rule in rules:
		rule_min, rule_max = rule.split('|')

		if number == rule_min:
			if rule_max in update:
				print(f"{rule=} for {rule_max=}")
				status = update.index(number) < update.index(rule_max)
				if not status:
					print(f"{rule=} failed")
					return status

	return True


def read_input(fname=None):
	if fname is None:
		input_text = test_input
	else:
		with open(fname) as f:
			input_text = f.read()
	rules, updates = input_text.split('\n\n')

	rules = rules.splitlines()
	updates = updates.splitlines()
	updates = [l.split(',') for l in updates]

	return rules, updates


def get_middle_page(update):
	return int(update[int((len(update) - 1) / 2)])


def main():
	rules, updates = read_input('input')
	# rules, updates = read_input()
	print(f"{rules=}")
	print(f"{updates=}")

	result = []
	for update in updates:
		r = []
		for number in update:
			number_valid = is_valid(number, update, rules)
			print(f"{number}: {number_valid}")
			r.append((number, number_valid))

		result.append(all([v for _, v in r]))

	valid_updates = [get_middle_page(update) for update, status_ok in zip(updates, result) if status_ok]
	for update, status_ok in zip(updates, result):
		if status_ok:
			print(update, get_middle_page(update))
	print(sum(valid_updates))
			

if __name__ == '__main__':
	main()