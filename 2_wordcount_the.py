'''
Write a MapReduce program that counts the number of times "the" appears in the file.
'''

from mrjob.job import MRJob

class MRTheFrequencyCount(MRJob):
	def mapper(self, _, line):
		line = line.split()
		counter = 0
		for word in line:
			if (word == "the"):
				counter += 1
		yield("the", counter)

	def reducer(self, key, values):
		yield key, sum(values)


if __name__ == '__main__':
	MRTheFrequencyCount.run()
