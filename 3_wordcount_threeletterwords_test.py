import csv

with open("example-sanderson.txt", 'r') as f:
	my_count = 0
	print("first", my_count)
	for line in f:
		words = line.split()
		for word in words:
			if len(word) == 3:
				print(my_count,word)
				my_count += 1
	print('the number of three-letter words in the text file is: ', my_count)	
