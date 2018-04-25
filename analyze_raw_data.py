if __name__ == '__main__':
	mulligans_in_top_three = [0, 0, 0, 0]
	position_of_mulligans = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	mulligan_in_single_repeat = [0, 0, 0]
	with open('./raw_data/raw_data_ll') as rdll:
		rd = eval(rdll.read())
	for m in rd:
		if m.count(0) == 2:
			if m[0] > 0:
				mulligan_in_single_repeat[0] += 1
			elif m[1] > 0:
				mulligan_in_single_repeat[1] += 1
			else:
				mulligan_in_single_repeat[2] += 1
		repeats = 0
		for i in range(len(m)):
			position_of_mulligans[i][m[i]] += 1
			if m[i] > 0:
				repeats += 1
		mulligans_in_top_three[repeats] += 1
	print('Distribution of 0/1/2/3 repeats in top three:')
	print([x/sum(mulligans_in_top_three) for x in mulligans_in_top_three])
	print('Distribution of the final spot of mulliganed card #1/2/3:')
	print([[x[0]/sum(mulligans_in_top_three), x[1]/sum(mulligans_in_top_three), x[2]/sum(mulligans_in_top_three), x[3]/sum(mulligans_in_top_three)] for x in position_of_mulligans])
	print('Proportion of mulliganed card #1/2/3 in top three when a single repeat occurs.')
	print([x/sum(mulligan_in_single_repeat) for x in mulligan_in_single_repeat])
