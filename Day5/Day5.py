import unittest

# Paul Armstrong

# Traverses the maze and counts how many steps it takes to escape
def part_one(maze):
	
	jump_count = 0;
	pos = 0;
	while (0 <= pos < len(maze)):
		# Sadly there is no post increment in python, so this must be done the long way
		maze[pos] += 1
		pos += maze[pos] - 1
		jump_count += 1
	
	return jump_count;

# Traverses the maze using part two rules and counts how many steps it takes to escape
def part_two(maze):

	jump_count = 0;
	pos = 0;
	while (0 <= pos < len(maze)):

		# Keep track of the old position to determine how it should be adjusted
		old_pos = pos
		pos += maze[pos]
		maze[old_pos] += (1 if (maze[old_pos] < 3) else -1)

		jump_count += 1
	
	return jump_count;



def main():
	input = open("input.txt")

	# Get a list of all phrases
	numbers = []
	for line in input:
		numbers.append(int(line.strip('\n')))

	# Print the results
	print("Part one: ", part_one(numbers.copy()))
	print("Part two: ", part_two(numbers.copy()))


class Day5Tests(unittest.TestCase):
	def test_part_one(self):
		inputs = [[0,3,0,1,-3]]
		outputs = [5]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_one(inputs[i]))

	def test_part_two(self):
		inputs = [[0,3,0,1,-3]]
		outputs = [10]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_two(inputs[i]))


if (__name__ == "__main__"):
	main()
	unittest.main()

