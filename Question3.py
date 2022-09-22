#Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new
#array of the same length with the squares of the original integers also sorted in ascending order.

def non_array_numbers(array):
	result = [0 for _ in array]
	left = 0
	right = len(array) - 1
	result_array = len(array) - 1
	while left <= right:
		if abs(array[left]) > abs(array[right]):
			result[result_array] = array[left] * 2
			left += 1
		else:
			result[result_array] = array[right] * 2
			right -= 1
		result_array -= 1
	return result

print(non_array_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

