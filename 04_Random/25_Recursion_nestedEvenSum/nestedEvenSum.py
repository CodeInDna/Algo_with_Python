# ---------------------- PROBLEM 25 (RANDOM) ----------------------------------#
# Write a function called nestedEvenSum. Return the sum of all even numbers in
# an object which may contain nested objects.

# Sample input: {'outer':2,
# 					'obj':{
# 						'inner':2,
# 						'otherobj':{
# 							'superInner': 2,
# 							'notANumber':true,
# 							'alsonotaNumber': "yup"
# 						}
# 					}
# 				}
# Sample output: 6

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def nestedEvenSum(in_dict, total=0):
	
	for key in list(in_dict.keys()):
		if isinstance(in_dict[key], dict):
			total += nestedEvenSum(in_dict[key])
		elif isinstance(in_dict[key], int) and in_dict[key] % 2 == 0:
			total += in_dict[key] 
	return total
# ----------------METHOD 01---------------------#