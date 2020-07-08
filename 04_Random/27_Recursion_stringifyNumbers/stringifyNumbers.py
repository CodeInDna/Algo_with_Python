# ---------------------- PROBLEM 27 (RANDOM) ----------------------------------#
# Write a function called stringifyNumbers which takes in object and finds all 
# of the values which are numbers and converts them to strings. Recursion would be 
# a great way to solve this.

# Sample input: {'num': 1,
				# 'test': [],
				# 'data': {
				# 	'val': 4,
				# 	'info':{
				# 		'isRight': True
				# 		'random': 66
				# 		}
				# 	}
				# }
# Sample output: {'num': "1",
				# 'test': [],
				# 'data': {
				# 	'val': "4",
				# 	'info':{
				# 		'isRight': True
				# 		'random': "66"
				# 		}
				# 	}
				# }

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def stringifyNumbers(in_dict):
	
	for key in list(in_dict.keys()):
		if len(in_dict) == 0: return in_dict

		if type(in_dict[key]) == dict:
			stringifyNumbers(in_dict[key]) 
		elif type(in_dict[key]) == int:
			in_dict[key] = str(in_dict[key])

	return in_dict
# ----------------METHOD 01---------------------#

dict1 = {'num': 1,
		'test': [],
		'data': {
			'val': 4,
			'info':{
				'isRight': True,
				'random': 66
				}
			}
		}

dict_ans = {'num': "1",
		'test': [],
		'data': {
			'val': "4",
			'info':{
				'isRight': True,
				'random': "66"
				}
			}
		}

print(stringifyNumbers(dict1))