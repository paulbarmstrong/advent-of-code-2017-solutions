import unittest

# Paul Armstrong

def part_one(target_num):
	# Traverse the spiral to find the coordinates of the number. Spiral format:
	#
	#		5 4 3
	#		6 1 2
	#		7 8 9
	#
	directions = [[1,0], [0,1], [-1,0], [0,-1]]
	dir_change_count = 0
	position = [0,0]
	pos_num = 1
	while pos_num < target_num:
		# Perform ([number of direction changes] // 2 + 1) movements per direction
		for t in range(0, (dir_change_count // 2) + 1):
			if (pos_num >= target_num):
				break
			# Move in the direction and add one to the position number
			position[0] += directions[dir_change_count % 4][0]
			position[1] += directions[dir_change_count % 4][1]
			pos_num += 1

		# Turn to the next direction
		dir_change_count += 1
		
	# Get the manhattan distance from the position
	return abs(position[0]) + abs(position[1])
	

def part_two(target_num):
	# Use a map (dictionary) to build and traverse the spiral to find the next highest number.
	# In this sprial the position's number is the surrounding 8 numbers combined:
	#
	#		5  4  2
	#		10 1  1
	#		11 23 25
	#
	spiral_dict = dict()
	spiral_dict[tuple([0,0])] = 1
	directions = [[1,0], [0,1], [-1,0], [0,-1]]
	dir_change_count = 0
	position = [0,0]
	pos_num = 1
	while pos_num <= target_num:
		# Perform ([number of direction changes] // 2 + 1) movements per direction
		for t in range(0, (dir_change_count // 2) + 1):
			if (pos_num > target_num):
				break
			# Move in the direction
			position[0] += directions[dir_change_count % 4][0]
			position[1] += directions[dir_change_count % 4][1]

			# Use the dictionary to determine the new position's number
			pos_num = 0
			for i in range(-1, 2):
				for j in range(-1, 2):
					temp_pos = position.copy()
					temp_pos[0] += i
					temp_pos[1] += j
					pos_num += spiral_dict.get(tuple(temp_pos), 0)

			# Map the new position to the new position number in the dictionary
			spiral_dict[tuple(position)] = pos_num

		# Turn to the next direction
		dir_change_count += 1

	# Return this pos_num (it is the largest after the target_num)
	return pos_num


def main():
	# Get the number
	target_num = int(open("input.txt").readline())

	# Print the results
	print("Part one: ", part_one(target_num))
	print("Part two: ", part_two(target_num))


class Day3Tests(unittest.TestCase):
	def test_part_one(self):
		inputs = [	1, 3, 6, 10]
		outputs = [	0, 2, 1, 3]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_one(inputs[i]))

	def test_part_two(self):
		inputs = [	1, 2, 23, 147]
		outputs = [	2, 4, 25, 304]
		for i in range(0, len(inputs)):
			self.assertEqual(outputs[i], part_two(inputs[i]))


if (__name__ == "__main__"):
	main()
	unittest.main()

