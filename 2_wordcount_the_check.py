import csv
import os

os.chdir('/Users/fanny/ncf/distcomp/hw/1_mapreduce_intro')

#with open('example-sanderson.txt', rewline='') as csvfile:
#	thereader = csv.reader(csvfile)
#	for row in thereader:
#		#print(row)	
#		#print(', '.join(row))
#		for word in row:
#			if word == 'the':
#				print('the')

#with open('/Users/fanny/ncf/distcomp/hw/map_reduce_intro/example-sanderson.txt', 'r') as f:
with open("example-shakespeare.txt", 'r') as f:
	count = 0
	for line in f:
		words = line.split()
		for i in words:
			if(i=="the"):
				count=count+1
	print('word count is:', count)
