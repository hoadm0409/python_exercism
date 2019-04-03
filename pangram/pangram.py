from string import ascii_lowercase

def is_pangram(sentence):
	alphabet = set([char for char in ascii_lowercase])
	chars = set([char for char in sentence.lower() if char in alphabet])
	return alphabet.issubset(chars)
