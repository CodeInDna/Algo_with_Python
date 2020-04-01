# ---------------------------------- PROBLEM 24 (MEDIUM) --------------------------------------#
# Suffix Trie Construction

# Write a class for a suffix-trie-like data structure. The class should have a "root" property set 
# to be the root node of the trie. The class should support creation from a string and the searching 
# of strings. The creation method (called populateSuffixTrieFrom()) will be called when the class is 
# instantiated and should populate the "root" property of the class. Note that every string added to 
# the trie should end with the special "endSymbol" character: "*".

# Sample input (for creation): "babc"
# Sample output (for creation):
# {
#    "c": {"*": True},
#    "b": {
#    "c": {"*": True},
#    "a": {"b": {"c": {"*": True}}},
# },
#    "a": {"b": {"c": {"*": True}}},
# }
# Sample input (for searching in the suffix trie above): "abc"
# Sample output (for searching in the suffix trie above): True

# ----------------METHOD 01---------------------#
class SuffixTrie:
	def __init__(self, string):
		self.root = {}
		self.endSymbol = '*'
		self.populateSuffixTrieFrom(string)

# COMPLEXITY = TIME: O(n^2), SPACE: O(n^2)
	def populateSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.insertSubstringStartingAt(i, string)

	def insertSubstringStartingAt(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			letter = string[j]
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = True

# COMPLEXITY = TIME: O(m), SPACE: O(1) where m = length of string searching for
	def contains(self, string):
		node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return self.endSymbol in node
# ----------------METHOD 01---------------------#