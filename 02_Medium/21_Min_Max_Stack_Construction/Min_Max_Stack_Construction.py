# ---------------------------------- PROBLEM 21 (MEDIUM) --------------------------------------#
# Min Max Stack Construction

# Write a Min Max Stack class. The class should support pushing and popping values on and off the 
# stack, peeking at values at the top of the stack, and getting both the minimum and the maximum 
# values in the stack. All class methods, when considered independently, should run in constant time 
# and with constant space.


class MinMaxStack:
	def __init__(self):
		self.minMaxStack = []
		self.stack = []

	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def peek(self):
		return self.stack[len(self.stack) - 1]

	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def pop(self):
		self.minMaxStack.pop()
		return self.stack.pop()

	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def push(self, num):
		newMinMax = {"min": num, "max":num}
		if len(self.minMaxStack):
			lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
			newMinMax["min"] = min(lastMinMax["min"], num)
			newMinMax["max"] = max(lastMinMax["max"], num)
		self.minMaxStack.append(newMinMax)
		self.stack.append(num)

	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def getMin(self):
		return self.minMaxStack[len(self.minMaxStack)-1]["min"]

	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def getMax(self):
		return self.minMaxStack[len(self.minMaxStack)-1]["max"]
