from analyze_screenshot_pairs import produce_raw_data as prd
import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:
		validation = 0
	else:
		validation = int(sys.argv[1])
	default = 11
	a = prd(default, validation)
	x = 0
	y = 0
	if validation == 0:
		while True:
			x += 1
			print('False negative comparison: ' + str(default-x))
			b = prd(default-x, validation)
			if a != b:
				print("False negative reached at: " + str(default-x))
				break
			if x > default:
				print("No false negative reached.")
				break
		while True:
			y += 1
			print('False positive comparison: ' + str(default+y))
			b = prd(default+y, validation)
			if a != b:
				print("False positive reached at: " + str(default+y))
				break
			if y + default > 31:
				print("No false positive reached.")
				break
	else:
		while True:
			x += 1
			print('False negative comparison: ' + str(default-x))
			b = prd(default-x, validation)
			if a.count('0') != b.count('0'):
				print("False negative reached at: " + str(default-x))
				break
			if x > default:
				print("No false negative reached.")
				break
		while True:
			y += 1
			print('False positive comparison: ' + str(default+y))
			b = prd(default+y, validation)
			if a.count('0') != b.count('0'):
				print("False positive reached at: " + str(default+y))
				break
			if y + default > 31:
				print("No false positive reached.")
				break
