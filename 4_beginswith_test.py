import csv
import string
import collections

with open("example-sanderson.txt", 'r') as f:
	my_list = []
	for line in f:
		words = line.split()
		for word in words:
			beginning_of_word = word[0].lower()
			my_list.append(beginning_of_word)
	c = collections.Counter(my_list)
	print (c)
