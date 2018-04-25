from os import replace
from glob import iglob
import sys

def enumerate_screenshot_pairs():
	print('Enumerating screenshots in pairs.')
	for fn in iglob('./data/*.png'):
		if fn[:19] == './data\\Screenshot (':
			x = 6
			while True:
				try:
					replace(fn, './data/ss' + str(int(fn[19:19+x])).zfill(6) + '.png')
					break
				except ValueError:
					x -= 1
					if x < 1:
						print('Invalid filename found. Aborting.')
						sys.exit()
	a = True
	i = 1
	for fn in iglob('./data/*.png'):
		replace(fn, './data/' + str(i).zfill(6) + ('a' if a else 'b') + '.png')
		i = i if a else i + 1
		a = not a
	print('Enumeration complete.')
