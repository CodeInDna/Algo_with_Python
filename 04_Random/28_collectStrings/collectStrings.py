# ---------------------- PROBLEM 28 (RANDOM) ----------------------------------#
# Write a function called collectStrings which accepts an object and returns an array
# of all the values in the object that have a typeof string.

# Sample input: {'num': 1,
# 				'stuff': "foo",
# 				'data': {
# 					'val': 4,
# 					'thing':{
# 						'info': "bar",
# 						'moreinfo': {
# 							'evenmoreinfo':{
# 									wemadeit: "baz"
# 								}
# 							}
# 						}
# 					}
# 				}
# Sample output: ["foo", "bar", "baz"]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def collectStrings(in_dict, arr=[]):
	if len(in_dict) == 0: return arr

	for key in list(in_dict.keys()):
		if type(in_dict[key]) == dict:
			return collectStrings(in_dict[key])
		elif type(in_dict[key]) == str:
			arr.append(in_dict[key])
	return arr
# ----------------METHOD 01---------------------#


dict1 = {'num': 1,
				'stuff': "foo",
				'data': {
					'val': 4,
					'thing':{
						'info': "bar",
						'moreinfo': {
							'evenmoreinfo':{
									'wemadeit': "baz"
							}
						}
					}
				}
		}

print(collectStrings(dict1))