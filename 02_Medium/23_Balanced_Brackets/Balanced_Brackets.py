# ---------------------------------- PROBLEM 23 (MEDIUM) --------------------------------------#
# Balanced Brackets

# Write a function that takes in a string made up of brackets ("(", "[", "{", ")", "]", and "}") 
# and other optional characters. The function should return a boolean representing whether or not 
# the string is balanced in regards to brackets. A string is said to be balanced if it has as many 
# opening brackets of a given type as it has closing brackets of that type and if no bracket is 
# unmatched. Note that a closing bracket cannot match a corresponding opening bracket that comes 
# after it. Similarly, brackets cannot overlap each other as in "[(])".

# Sample input: "([])(){}(())()()"
# Sample output: True (it is balanced)

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n)
def balancedBrackets(string):
	openingBracks = '({['
	closingBracks = ')}]'
	matchingBrackets = {')':'(', '}':'{', ']':'['}
	stack = []
	for brack in string:
		if brack in openingBracks:
			stack.append(brack)
		elif brack in closingBracks:
			if len(stack) == 0:
				return False
			elif stack[-1] == matchingBrackets[brack]:
				stack.pop()
			else:
				return False
	return len(stack) == 0
# ----------------METHOD 01---------------------#