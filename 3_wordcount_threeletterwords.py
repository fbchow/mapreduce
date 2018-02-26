'''
count the number of three letter words
'''

from mrjob.job import MRJob

class MRThreeLetterWordFrequencyCount(MRJob):
	
	def mapper(self, _, line):
		counter = 0
		line  = line.split()
		for word in line:
			if len(word) == 3:
				print(word)
				counter += 1 
		yield ("3", counter)

	def reducer(self, key, values):
		yield key, sum(values)

if __name__ == '__main__':
	MRThreeLetterWordFrequencyCount.run()
