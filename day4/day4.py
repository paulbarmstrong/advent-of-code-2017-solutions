import unittest

# Paul Armstrong

def part_one(phrases):

	# Keep track of the number of valid phrases
	valid_phrase_count = 0

	for phrase in phrases:

		word_list = phrase.strip('\n').split(' ')
		has_repeat = False

		# This will be a set of words
		words_set = set()

		# Fill the set with words
		for word in word_list:

			# If the word is already in the set, there is a repeat
			if (word in words_set):
				has_repeat = True
			words_set.add(word)
		
		if (not has_repeat):
			valid_phrase_count += 1
	
	return valid_phrase_count;

def part_two(phrases):

	# Keep track of the number of valid phrases
	valid_phrase_count = 0

	for phrase in phrases:

		word_list = phrase.strip('\n').split(' ')
		has_anagram = False

		# This will be a set of sorted word tuples
		words_set = set()

		# Fill the set with words and flag if there are any repeats
		for word in word_list:

			sorted_letters = list(word)
			sorted_letters.sort()
			sorted_letters = tuple(sorted_letters)

			# If the sorted_letters is already in the set, there is an anagram
			if (sorted_letters in words_set):
				has_anagram = True
			words_set.add(sorted_letters)
		
		if (not has_anagram):
			valid_phrase_count += 1
	
	return valid_phrase_count;



def main():
	input = open("input.txt")

	# Get a list of all phrases
	phrases = []
	for line in input:
		phrases.append(line)

	# Print the results
	print("Part one: ", part_one(phrases.copy()))
	print("Part two: ", part_two(phrases.copy()))


class Day4Tests(unittest.TestCase):
	def test_part_one(self):
		inputs = [["aa bb cc dd ee"], ["aa bb cc dd aa"], ["aa bb cc dd aaa","","ee rree"]]
		outputs = [1, 0, 3]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_one(inputs[i]))

	def test_part_two(self):
		inputs = [["abcde fghij"], ["abcde xyz ecdab"], ["a ab abc abd abf abj"], ["iiii oiii ooii oooi oooo"], ["oiii ioii iioi iiio"]]
		outputs = [1, 0, 1, 1, 0]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_two(inputs[i]))


if (__name__ == "__main__"):
	main()
	unittest.main()

