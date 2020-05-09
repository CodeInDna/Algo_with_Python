# ---------------------------------- PROBLEM 13 (HARD)--------------------------------------#
# Find Loop

# Write a function that takes in the head of a Singly Linked List that contains a loop (in other 
# words, the list's tail node points to some node in the list instead of the None (null) value). 
# The function should return the node (the actual node - not just its value) from which the loop 
# originates in constant space. Note that every node in the Singly Linked List has a "value" property 
# storing its value as well as a "next" property pointing to the next node in the list.

# Sample input:
# n0 -> n1 -> n2 -> n3 -> n4 -> n5 -> n6
#              ^    v
#             n9 <- n8 <- n7
# Sample output: n4

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def findLoop(head):
	first = head.next
	second = head.next.next
	while first != second:
		first = first.next
		second = second.next.next
	first = head
	while first != second:
		first = first.next
		second = second.next
	return first
# ----------------METHOD 01---------------------#