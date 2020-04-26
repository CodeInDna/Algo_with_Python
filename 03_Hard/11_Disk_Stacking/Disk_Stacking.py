# ---------------------------------- PROBLEM 11 (HARD)--------------------------------------#
# Disk Stacking

# You are given a non-empty array of arrays. Each subarray holds three integers and represents 
# a disk. These integers denote each disk's width, depth, and height, respectively. Your goal is 
# to stack up the disks and to maximize the total height of the stack. A disk must have a strictly 
# smaller width, depth, and height than any other disk below it. Write a function that returns an 
# array of the disks in the final stack, starting with the top disk and ending with the bottom disk. 
# Note that you cannot rotate disks; in other words, the integers in each subarray must represent 
# [width, depth, height] at all times. Assume that there will only be one stack with the greatest 
# total height.

# Sample input: [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 2, 1], [4, 4, 5]]
# Sample output: [[2, 1, 2], [3, 2, 3], [4, 4, 5]]

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n^2), SPACE: O(n)
def diskStacking(disks):
	disks.sort(key = lambda disk:disk[2])
	heights = [disk[2] for disk in disks]
	sequences = [None] * len(disks)
	for i in range(1, len(disks)):
		currentDisk = disks[i]
		for j in range(i):
			otherDisk = disks[j]
			if areValidDim(otherDisk, currentDisk):
				if heights[i] <= currentDisk[2] + heights[j]:
					heights[i] = currentDisk[2] + heights[j]
					sequences[i] = j
	return buildSequences(disks, sequences, heights.index(max(heights)))

def areValidDim(o, c):
	return (o[0] < c[0]) and (o[1] < c[1]) and (o[2] < c[2]) 

def buildSequences(disks, seq, maxHeightIdx):
	sequences = []
	while maxHeightIdx is not None:
		sequences.append(disks[maxHeightIdx])
		maxHeightIdx = seq[maxHeightIdx]
	return list(reversed(sequences))
# ----------------METHOD 01---------------------#