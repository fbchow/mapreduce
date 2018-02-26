'''
Write a MapReduce program that counts the number of words that begin with each letter. 
(That is, how many words start with 'a'? How many words start with 'b'? 
'''

from mrjob.job import MRJob
import collections

class MRWordBeginsWithFrequencyCount(MRJob):

	def mapper(self, _, line):
		line = line.split()
#		my_list = [] 
		for word in line:
			beginning_of_word = word[0].lower()
			yield (beginning_of_word, 1)
		#	my_list.append(beginning_of_word)	
		#yield("beginning_chars", my_list)
		#yield(my_list, 'stuff')  

	def reducer(self, key, values):
		#my_list = []
		
		#for p in values:
		#	my_list.append(p)
	#	count = collections.Counter(my_list)	
		yield (key, sum(values)) 
#		yield collections.Counter(values)

if __name__ == '__main__':
	MRWordBeginsWithFrequencyCount.run()	
