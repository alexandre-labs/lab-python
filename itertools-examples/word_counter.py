import collection
import itertools


# in this case, I'd prefer to use collections
def word_counter(*words):
	'''Write a Python program that inputs a list of words, separated by white-
	space, and outputs how many times each word appears in the list.
		
	'''
	return dict(collections.Counter(words).items())


def word_counter_itertools(*words):
	'''Write a Python program that inputs a list of words, separated by white-
	space, and outputs how many times each word appears in the list.
		
	'''
	return {
		word: len(list(word_group)) for word, word_group in itertools.groupby(
			sorted(words), key=lambda x: x)
	} 
