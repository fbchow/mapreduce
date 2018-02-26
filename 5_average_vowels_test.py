import csv

with open("example-sanderson.txt", 'r') as f:
	count = 0
	vowels = ('a','e','i','o','u')
	for line in f:
		words = line.split()
		for word in words:
			for char in word:
				if char in vowels:
 					count += 1	
	print('the number of vowels in the text file is: ', count)	

