# ---------------------------------- PROBLEM 10 (HARD)--------------------------------------#
# Knapsack Problem

# You are given an array of arrays. Each subarray in this array holds two integer values and 
# represents an item; the first integer is the item's value, and the second integer is the item's 
# weight. You are also given an integer representing the maximum capacity of a knapsack that you have. 
# Your goal is to fit items in your knapsack, all the while maximizing their combined value. Note that 
# the sum of the weights of the items that you pick cannot exceed the knapsack's capacity. Write a 
# function that returns the maximized combined value of the items that you should pick, as well as an 
# array of the indices of each item picked. Assume that there will only be one combination of items 
# that maximizes the total value in the knapsack.

# Sample input: [[1, 2], [4, 3], [5, 6], [6, 7]], 10
# Sample output: [10, [1, 3]]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(Nc), SPACE: O(Nc), where N i the number of items and c is the capacity
def knapsackProblem(lst_Items, target_cap):
	knapsackValues = [[0 for _ in range(target_cap + 1)] for _ in range(len(lst_Items) + 1)]
	for i in range(1, len(lst_Items) + 1):
		currentWeight = lst_Items[i - 1][1]
		currentValue = lst_Items[i - 1][0]
		for cap in range(target_cap + 1):
			if currentWeight > cap:
				knapsackValues[i][cap] = knapsackValues[i - 1][cap]
			else:
				knapsackValues[i][cap] = max(knapsackValues[i - 1][cap], knapsackValues[i - 1][cap - currentWeight] + currentValue)
	return [knapsackValues[-1][-1], getKnapsackItems(knapsackValues, lst_Items)]			

def getKnapsackItems(knapsackValues, items):
	result = []
	i = len(knapsackValues) - 1
	c = len(knapsackValues[0]) - 1
	while i > 0:
		if knapsackValues[i][c] == knapsackValues[i - 1][c]:
			i -= 1 
		else:
			result.append(i - 1)
			c -= items[i - 1][1]
			i -= 1
		if c == 0:
			break
	return list(reversed(result))
# ----------------METHOD 01---------------------#
