# ---------------------- PROBLEM 2 (RANDOM) ----------------------------------#
# Write a function called coinChange which accepts two parameters: an array of 
# denominations and a value. The function should return the number of ways you can 
# obtain the value from the given collection of denominations. You can think of 
# this as figuring out the number of ways to make change for a given value from a 
# supply of coins. 

# Sample input: [1, 5, 10, 25], 5
# Sample output: 2

# ----------------METHOD 01---------------------#
# Using Divide and Conquer
# COMPLEXITY = TIME: O(n^2 ), SPACE: O(1)
def coinChange(denoms, num):
	ways = [0] * (num+1)
	ways[0] = 1
	for denom in denoms:
		for amount in range(1, num + 1):
			if denom <= amount:
				ways[amount] += ways[amount - denom]
	return ways[num]
# ----------------METHOD 01---------------------#
print(coinChange([1, 5, 10, 25], 5))