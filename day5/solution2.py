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


def is_valid_number(number, update, rules):
	for rule in rules:
		rule_min, rule_max = rule.split('|')

		if number == rule_min:
			if rule_max in update:
				# print(f"{rule=} for {rule_max=}")
				status = update.index(number) < update.index(rule_max)
				if not status:
					# print(f"{rule=} failed")
					return status
	return True


def is_valid_update(update, rules):
	r = []
	for number in update:
		number_valid = is_valid_number(number, update, rules)
		print(f"{number}: {number_valid}")
		r.append((number, number_valid))

	return all([v for _, v in r])


def fix_update(update, rules):
	if is_valid_update(update, rules):
		print("update is valid")
		return update

	fixed_update = update
	for number in fixed_update:
		if not is_valid_number(number, update, rules):
			fixed_update = check_fix_number(number, update, rules)

	while not is_valid_update(fixed_update, rules):
		fixed_update = fix_update(update, rules)

	return fixed_update


def check_fix_number(number, update, rules):
	for rule in rules:
		rule_min, rule_max = rule.split('|')

		if number == rule_min:
			if rule_max in update:
				print(f"{rule=} for {rule_max=}")
				status = update.index(number) < update.index(rule_max)

				# fix
				if not status:
					print(f"{rule=} failed")
					update[update.index(number)], update[update.index(rule_max)] = update[update.index(rule_max)], update[update.index(number)]
					print(f"fixed: {update}")
					return update
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

	statuses = []

	for update in updates:
		r = []
		for number in update:
			number_valid = is_valid_number(number, update, rules)
			r.append((number, number_valid))

		statuses.append(all([v for _, v in r]))

	invalid_updates = [update for update, status_ok in zip(updates, statuses) if not status_ok]
	print(invalid_updates)

	# fix
	fixed_updates = [fix_update(u, rules) for u in invalid_updates]
	print(f"{fixed_updates=}")
	print(sum([get_middle_page(update) for update in fixed_updates]))
			

if __name__ == '__main__':
	main()