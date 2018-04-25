from enumerate_screenshot_pairs import enumerate_screenshot_pairs as esp
from validate_screenshot_pairs import validate_screenshot_pairs as vsp
from os import replace

if __name__ == '__main__':
	esp()
	faulty_screenshot_pairs = vsp()
	print('The following screenshot pairs have been identified as faulty:')
	print(faulty_screenshot_pairs)
	print('Moving the faulty screenshot pairs from /data/ to /faulty_screenshot_pairs/')
	for i in faulty_screenshot_pairs:
		replace('./data/' + str(i).zfill(6) + 'a.png', './faulty_screenshot_pairs/' + str(i).zfill(6) + 'a.png')
		replace('./data/' + str(i).zfill(6) + 'b.png', './faulty_screenshot_pairs/' + str(i).zfill(6) + 'b.png')
	print('Finished moving the faulty screenshot pairs.')
	print('Re-enumerating.')
	esp()
