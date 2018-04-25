from analyze_screenshot_pairs import produce_raw_data as prd

def validate_screenshot_pairs():
	faulty_screenshot_pairs = []
	limit = 11
	i = 0
	n = 0
	a = True
	print('Searching for faulty screenshots.')
	for c in prd(limit, 1):
		i = i + 1 if a else i
		a = not a
		if c == '0':
			n += 1
			print('Fault found in screenshot pair: ' + str(i))
			faulty_screenshot_pairs.append(i)
	if n == 0:
		print('No faulty mulligans found.')
	i = 0
	n = 0
	print('Searching for faulty mulligans.')
	for c in prd(limit, 2):
		i += 1
		if c == '0':
			n += 1
			print('Faulty mulligan found in screenshot pair: ' + str(i))
			faulty_screenshot_pairs.append(i)
	if n == 0:
		print('No faulty mulligans found.')
	return sorted(list(set(faulty_screenshot_pairs)))
