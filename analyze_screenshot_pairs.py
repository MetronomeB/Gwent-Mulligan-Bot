from glob import glob
from PIL import Image
import dhash

def crop(n, validation):
	xc = [[195, 353], [429, 587], [663, 822]]
	yc = [[312, 509]]
	xv = [[983, 1018], [754, 789]]
	yv = [[972, 1069]]
	crops = [[], []]
	with Image.open('./data/' + str(n).zfill(6) + 'a.png') as imga, Image.open('./data/' + str(n).zfill(6) + 'b.png') as imgb:
		if validation == 1:
			crops[0].append(imga.crop((0, 0, 180, 1079)))
			crops[0].append(imgb.crop((0, 0, 180, 1079)))
			with Image.open('./reference_images/reference.png') as ref:
				crops[1].append(ref.copy())
				crops[1].append(ref.copy())
		elif validation == 2:
			crops[0].append(imga.crop((xv[0][0], yv[0][0], xv[0][1], yv[0][1])))
			crops[1].append(imgb.crop((xv[1][0], yv[0][0], xv[1][1], yv[0][1])))
		else:
			for i in range(len(xc)):
				crops[0].append(imga.crop((xc[i][0], yc[0][0], xc[i][1], yc[0][1])))
				crops[1].append(imgb.crop((xc[i][0], yc[0][0], xc[i][1], yc[0][1])))
	return crops

def hash_crops(crops):
	hashes = [[], []]
	for i in range(len(crops)):
		for j in range(len(crops[i])):
			row, col = dhash.dhash_row_col(crops[i][j])
			hashes[i].append(dhash.format_hex(row, col))
	return hashes

def find_repeats(hashes, limit):
	repeat_at = ''
	for i in range(len(hashes[0])):
		repeat_found = False
		for j in range(len(hashes[1])):
			hamming_distance = 0
			for k in range(len(hashes[0][i])):
				if hashes[0][i][k] != hashes[1][j][k]:
					hamming_distance += 1
			if hamming_distance <= limit:
				repeat_at += str(j + 1)
				repeat_found = True
				break
		if not repeat_found:
			repeat_at += str(0)
	return repeat_at

def produce_raw_data(limit, validation):
	raw_data = ''
	for i in range(int(len(glob('./data/*.png'))/2)):
		raw_data += find_repeats(hash_crops(crop(i + 1, validation)), limit)
	return raw_data
