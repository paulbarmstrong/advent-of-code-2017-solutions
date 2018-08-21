import unittest

# Paul Armstrong

def part_one(rows):
	# Find the check_sum by adding difference between max and min in each row
	check_sum = 0
	for row in rows:
		check_sum += max(row) - min(row)
	return check_sum
			
def part_two(rows):
	# Find the even_div_sum by adding the division of the one divisible combination
	even_div_sum = 0
	for row in rows:
		for i in range(0, len(row)):
			for j in range(0, len(row)):
				if i != j and row[i] % row[j] == 0:
					even_div_sum += row[i] // row[j]
	return even_div_sum


def main():
	input = open("input.txt")

	# Fill rows with all of the rows of numbers
	rows = []
	for line in input:
		rows.append(list(map(int, line.strip('\n').split('\t'))))

	# Print the results
	print("Part one: ", part_one(rows.copy()))
	print("Part two: ", part_two(rows.copy()))

class Day1Tests(unittest.TestCase):
	def test_part_one(self):
		inputs = [[[5,1,9,5],[7,5,3],[2,4,6,8]]]
		outputs = [18]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_one(inputs[i]))

	def test_part_two(self):
		inputs = [[[5,9,2,8],[9,4,7,3],[3,8,6,5]]]
		outputs = [9]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_two(inputs[i]))

	
if (__name__ == "__main__"):
	main()
	unittest.main()
