def word_frequency(filename):
	file1 = open(filename,"r+")
	lines = file1.readlines()
	print(lines)
	total = {}
	for line in lines:
		res = line.split()
		for word in res:
			if not total.get(word):
				total[word] = 1
			else:
				temp = total.get(word)
				temp += 1
				total[word] = temp

	myKeys = list(total.keys())
	myKeys.sort()
	sorted_dict = {i: total[i] for i in myKeys}
	print(sorted_dict)
	return sorted_dict