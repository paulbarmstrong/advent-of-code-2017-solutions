import unittest

# Paul Armstrong

def part_one(nums):
	# Add up all of the numbers which repeat
	total = 0
	length = len(nums)
	for i in range(0, length):
		if nums[i] == nums[(i + 1) % length]:
			total += nums[i]
	return total

def part_two(nums):
	# Add up all of the numbers which match half way around
	total = 0
	length = len(nums)
	for i in range(0, length):
		if nums[i] == nums[(i + (length // 2)) % length]:
			total += nums[i]
	return total


def main():
	input = open("input.txt")

	# Fill nums with all of the numbers in the input
	nums = []
	for line in input:
		for ch in line.strip('\n'):
			nums.append(int(ch))

	# Print the results
	print("Part one: ", part_one(nums.copy()))
	print("Part two: ", part_two(nums.copy()))

class Day1Tests(unittest.TestCase):
	def test_part_one(self):
		inputs = [[1,1,2,2],	[1,1,1,1],	[1,2,3,4],	[9,1,2,1,2,1,2,9]]
		outputs = [3,			4,			0,			9]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_one(inputs[i]))

	def test_part_two(self):
		inputs = [[1,2,1,2],	[1,2,2,1],	[1,2,3,4,2,5],	[1,2,3,1,2,3],	[1,2,1,3,1,4,1,5]]
		outputs = [6,			0,			4,				12,				4]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_two(inputs[i]))

	
if (__name__ == "__main__"):
	main()
	unittest.main()
