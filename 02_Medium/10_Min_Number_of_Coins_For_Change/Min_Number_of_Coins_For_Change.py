# ---------------------------------- PROBLEM 10 (MEDIUM) --------------------------------------#
# Min Number of Coins for Change
# Given an array of positive integers representing coin denominations and a single non-negative 
# integer representing a target amount of money, implement a function that returns the smallest 
# number of coins needed to make change for that target amount using the given coin denominations. 
# Note that an unlimited amount of coins is at your disposal. If it is impossible to make change 
# for the target amount, return -1.

# Sample input: 7, [1, 5, 10]
# Sample output: 3 (2x1 + 1x5)

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1) 
def minNumberOfCoinsForChange(num, denoms):
	numOfCoins = [float("inf") for i in range(num + 1)]
	numOfCoins[0] = 0
	for denom in denoms:
		for amount in range(num + 1):
			if denom <= amount:
				numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
	return numOfCoins[num] if numOfCoins[num] != float("inf") else -1
# ----------------METHOD 01---------------------#
print(minNumberOfCoinsForChange(6, [1, 2, 4]))
