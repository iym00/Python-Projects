# Creating a function that takes in a list of integers and adds 10 to all odd numbers and returns the list (iterative style)
def is_odd_add_10_return_list_iterative(integer_list):
	# Iterating through the list using a for loop
	for i in range(len(integer_list)):
		# Checking if the number in the index i is odd or not
		if integer_list[i] % 2 != 0:
			# If yes, we increment by 10
			integer_list[i] += 10
	# Return the list
	return integer_list



def recursively_defined_version_of_the_first_function(integer_list):
	# Base cases
	if len(integer_list) == 0 or (len(integer_list) == 1 and integer_list[0] % 2 == 0):
		return integer_list
	
	# Recursive case
	else:
		# work to do (after simplification)
		if len(integer_list) == 1:
			integer_list[0] += 10
			return integer_list
		
		else:
			# Creating new list to hold integers
			new_list = []
			# Dividing the given integer list by two (simplifying step)
			first_half = integer_list[:len(integer_list)//2]
			second_half = integer_list[len(integer_list)//2:]
			# Recursive call
			first_half_simplified = recursively_defined_version_of_the_first_function(first_half)
			second_half_simplified = recursively_defined_version_of_the_first_function(second_half)
			# work to do (after simplification)
			new_list += first_half_simplified + second_half_simplified
			# Return list
			return new_list
				
	


	
