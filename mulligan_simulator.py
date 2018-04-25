from random import randint
import sys

def m1a(mulligans):
	global mulligans_in_top_three, position_of_mulligans, mulligan_in_single_repeat
	deck = [0] * 16
	repeats = 0
	for i in range(mulligans):
		deck.insert(randint(0, len(deck)), i + 1)
		del deck[deck.index(0)]
	for i in range(mulligans):
		if deck.index(i+1) < 3:
			repeats += 1
			position_of_mulligans[i][deck.index(i+1)+1] += 1
		else:
			position_of_mulligans[i][0] += 1
	mulligans_in_top_three[repeats] += 1
	if repeats == 1:
		mulligan_in_single_repeat[sum(deck[:3]) - 1] += 1

def m1b(mulligans):
	global mulligans_in_top_three, position_of_mulligans, mulligan_in_single_repeat
	deck = [0] * 16
	repeats = 0
	for i in range(mulligans):
		del deck[deck.index(0)]
		deck.insert(randint(0, len(deck)), i + 1)
	for i in range(mulligans):
		if deck.index(i+1) < 3:
			repeats += 1
			position_of_mulligans[i][deck.index(i+1)+1] += 1
		else:
			position_of_mulligans[i][0] += 1
	mulligans_in_top_three[repeats] += 1
	if repeats == 1:
		mulligan_in_single_repeat[sum(deck[:3]) - 1] += 1

def m2(mulligans):
	global mulligans_in_top_three, position_of_mulligans, mulligan_in_single_repeat
	deck = [0] * 13
	repeats = 0
	for i in range(mulligans):
		deck.insert(randint(0, len(deck)), i + 1)
	for i in range(mulligans):
		if deck.index(i+1) < 3:
			repeats += 1
			position_of_mulligans[i][deck.index(i+1)+1] += 1
		else:
			position_of_mulligans[i][0] += 1
	mulligans_in_top_three[repeats] += 1
	if repeats == 1:
		mulligan_in_single_repeat[sum(deck[:3]) - 1] += 1

if __name__ == '__main__':
	mulligans_in_top_three = [0, 0, 0, 0]
	position_of_mulligans = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	mulligan_in_single_repeat = [0, 0, 0]
	mulligans = 3
	simulations = 10 ** int(sys.argv[1])
	if sys.argv[2] == '1a':
		print('Performing ' + str(simulations) + ' simulations of mulligan implementation M1a')
		for x in range(simulations):
			m1a(mulligans)
	elif sys.argv[2] == '1b':
		print('Performing ' + str(simulations) + ' simulations of mulligan implementation M1b')
		for x in range(simulations):
			m1b(mulligans)
	else:
		print('Performing ' + str(simulations) + ' simulations of mulligan implementation M2')
		for x in range(simulations):
			m2(mulligans)
	print('Distribution of 0/1/2/3 repeats in top three:')
	print([x/simulations for x in mulligans_in_top_three])
	print('Distribution of the final spot of mulliganed card #1/2/3:')
	print([[x[0]/simulations, x[1]/simulations, x[2]/simulations, x[3]/simulations] for x in position_of_mulligans])
	print('Proportion of mulliganed card #1/2/3 in top three when a single repeat occurs.')
	print([x/sum(mulligan_in_single_repeat) for x in mulligan_in_single_repeat])
