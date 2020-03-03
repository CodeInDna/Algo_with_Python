# ---------------------------------- PROBLEM 17 (MEDIUM) --------------------------------------#
# Remove Kth Node From End

# Write a function that takes in the head of a Singly Linked List and an integer k (assume that the 
# list has at least k nodes). The function should remove the kth node from the end of the list. 
# Note that every node in the Singly Linked List has a "value" property storing its value as well as 
# a "next" property pointing to the next node in the list or None (null) if it is the tail of the list.

# Sample input: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, 4
# Sample output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9

# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(1)
def removeKthNodeFromEnd(head, k):
	counter = 1 
	first = head
	second = head
	while counter <= k:
		second = second.next
		counter += 1
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while second.next is not None:
		second = second.next
		first = first.next
	first.next = first.next.next
	return head
# ----------------METHOD 01---------------------#