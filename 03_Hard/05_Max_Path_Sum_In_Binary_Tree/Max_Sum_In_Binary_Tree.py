# ---------------------------------- PROBLEM 5 (HARD) --------------------------------------#
# Max Path Sum In Binary Tree

# Write a function that takes in a Binary Tree and returns its max path sum. A path is a collection 
# of connected nodes where no node is connected to more than two other nodes; a path sum is the sum 
# of the values of the nodes in a particular path. Each Binary Tree node has a value stored in a 
# property called "value" and two children nodes stored in properties called "left" and "right," 
# respectively. Children nodes can either be Binary Tree nodes themselves or the None (null) value.

# Sample Input:
#       1
#       /\
#       2 3
#      /\ /\
#     4 5 6 7

# Sample output: 18
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i = 0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self
# ----------------METHOD 01---------------------#
# COMPLEXITY = TIME: O(), SPACE: O()
def maxPathSum(btree):
	pass

# ----------------METHOD 01---------------------#
test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
print(maxPathSum(test), 18)