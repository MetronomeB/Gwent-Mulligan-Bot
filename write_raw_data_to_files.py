from analyze_screenshot_pairs import produce_raw_data as prd

if __name__ == '__main__':
	raw_data = prd(11, 0)
	rd_ls = [raw_data[(x*3):(x+1)*3] for x in range(int(len(raw_data)/3))]
	rd_ll = [[int(rd_ls[x][0]), int(rd_ls[x][1]), int(rd_ls[x][2])] for x in range(len(rd_ls))]
	rd_csv = ''
	for m in rd_ll:
		for n in m:
			rd_csv += str(n) + ','
		rd_csv += '\n'
	with open('./raw_data/raw_data', 'w', encoding='utf8') as rd, open('./raw_data/raw_data_ls', 'w', encoding='utf8') as rdls, open('./raw_data/raw_data_ll', 'w', encoding='utf8') as rdll, open('./raw_data/raw_data.csv', 'w', encoding='utf8') as rdcsv:
		rd.write(raw_data)
		rdls.write(str(rd_ls))
		rdll.write(str(rd_ll))
		rdcsv.write(rd_csv)
