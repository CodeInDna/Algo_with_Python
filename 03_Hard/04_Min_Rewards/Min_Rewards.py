# ---------------------------------- PROBLEM 4 (HARD) --------------------------------------#
# Min Rewards

# Imagine that you're a teacher who's just graded the final exam in a class. You have a list of 
# student scores on the final exam in a particular order (not necessarily sorted), and you want 
# to reward your students. You decide to do so fairly by giving them arbitrary rewards following 
# two rules: first, all students must receive at least one reward; second, any given student must 
# receive strictly more rewards than an adjacent student (a student immediately to the left or to 
# 	the right) with a lower score and must receive strictly fewer rewards than an adjacent student 
# with a higher score. Assume that all students have different scores; in other words, the scores 
# are all unique. Write a function that takes in a list of scores and returns the minimum number 
# of rewards that you must give out to students, all the while satisfying the two rules.

# Sample input: [8,4 , 2, 1, 3, 6, 7, 9, 5]
# Sample output: 25 ([4, 3, 2, 1, 2, 3, 4, 5, 1])

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(n), n is the length of input array
def minRewards(scores):
	rewards = [1 for _ in scores]
	for curr in range(1, len(scores)):
		prev = curr - 1
		if scores[curr] > scores[prev]:
			rewards[curr] = rewards[prev] + 1
		else:
			while prev >= 0  and scores[prev] > scores[prev + 1]:
				rewards[prev] = max(rewards[prev], rewards[prev + 1] + 1)
				prev -= 1 
	return sum(rewards)
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n), n is the length of input array
#  Description: search local minimums(left and right of a number is greater than itself), 
#  iterate its left and right until peak is found.
def minRewards(scores):
	rewards = [1 for _ in scores]
	localMinIdxs = getLocalMinIdxs(scores)
	for loc_min_idx in localMinIdxs:
		expandFromLocMins(loc_min_idx, scores, rewards)
	return sum(rewards)

def getLocalMinIdxs(scores):
	localMinIdxs = []
	if len(scores) == 1:
		return [0]
	for idx in range(len(scores)):
		if idx == 0 and (scores[idx] < scores[idx + 1]):
			localMinIdxs.append(idx)
		elif (idx == len(scores) - 1) and (scores[idx] < scores[idx - 1]):
			localMinIdxs.append(idx)
		elif (scores[idx - 1] > scores[idx]) and (scores[idx + 1] > scores[idx]):
			localMinIdxs.append(idx)
		else:
			continue
	return localMinIdxs

def expandFromLocMins(locMinIdx, scores, rewards):
	leftIdx = locMinIdx - 1
	rightIdx = locMinIdx + 1
	while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
		rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
		leftIdx -= 1
	while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1]:
		rewards[rightIdx] = rewards[rightIdx - 1] + 1
		rightIdx += 1
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n), n is the length of input array
# Description: First go from left to right then right to left.
def minRewards(scores):
	rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		if scores[i] > scores[i - 1]:
			rewards[i] = rewards[i - 1] + 1
	for j in reversed(range(len(scores) - 1)):
		if scores[j] > scores[j + 1]:
			rewards[j] = max(rewards[j], rewards[j + 1] + 1)
	return sum(rewards)
# ----------------METHOD 03---------------------#