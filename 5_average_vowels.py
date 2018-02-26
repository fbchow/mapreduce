'''
Write a MapReduce program that for each possible word length computes the average number of vowels in the word. 
(That is, words with 4 letters typically have how many vowels? Words with 5 letters typically have how many vowels?)
'''

from mrjob.job import MRJob

class MRAverageVowelCount(MRJob):
	
	def mapper(self, _, line):
		line = line.split()
		# for word in line:
		# 	yield(len(word), word.lower())

		vowels = ('a','e','i','o','u')
		for word in line:
			vowel_count = 0
			for char in word:
				if char in vowels:
					vowel_count += 1
			yield (len(word), vowel_count)


	def reducer(self, key, values):
		values = list(values)	# convert values from generator to list class
		# yield key, average(values)
		yield key, sum(values) / len(values)

if __name__ == '__main__':
	MRAverageVowelCount.run()
