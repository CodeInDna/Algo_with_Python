# ---------------------- PROBLEM 47 (RANDOM) ----------------------------------#
# n computing, a hash table (hash map) is a data structure that implements an 
# associative array abstract data type, a structure that can map keys to values. 
# A hash table uses a hash function to compute an index, also called a hash code, 
# into an array of buckets or slots, from which the desired value can be found.

class HashTable:
	def __init__(self, size=4):
		self.keyMap = [None] * size 

# ----------------METHOD 01---------------------#
	# COMPLEXITY = AVERAGE/BEST TIME: O(1), WORST TIME: O(n), SPACE: O(1)
	def hash(self, key):
		total, WEIRD_PRIME = 0, 31
		for i in range(min(len(key), 100)):
			char = key[i]
			value = ord(char) - 96
			total = (total * WEIRD_PRIME + value) % len(self.keyMap)
		return total
# ----------------METHOD 01---------------------#

# ----------------METHOD 02---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def set(self, key, value):
		hashed_key = self.hash(key)
		if self.keyMap[hashed_key] is None:
			self.keyMap[hashed_key] = []
		self.keyMap[hashed_key].append([key,value])
		
		return self.keyMap[hashed_key]
# ----------------METHOD 02---------------------#

# ----------------METHOD 03---------------------#
	# COMPLEXITY = TIME: O(1), SPACE: O(1)
	def get(self, key):
		hashed_key = self.hash(key)
		idx = self.keyMap[hashed_key]
		if idx is not None:
			for pair in idx:
				if key == pair[0]: return pair[1]
		return None
# ----------------METHOD 03---------------------#

# ----------------METHOD 04---------------------#
	# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
	def keys(self):
		keyArr = []
		pair_list = self.keyMap
		for lst in pair_list:
			if lst:
				for key in lst: 
					if key[0] not in keyArr: keyArr.append(key[0])
		return keyArr
# ----------------METHOD 04---------------------#

# ----------------METHOD 05---------------------#
	# COMPLEXITY = TIME: O(n^2), SPACE: O(1)
	def values(self):
		valArr = []
		pair_list = self.keyMap
		for lst in pair_list:
			if lst:
				for val in lst: 
					if val[1] not in valArr: valArr.append(val[1])
		return valArr
# ----------------METHOD 05---------------------#


hashNo = HashTable()
print(hashNo.set('red', '#FF0000')) 	 # [['red', '#FF0000']]
print(hashNo.set('red', '#FF0000')) 	 # [['red', '#FF0000'], ['red', '#FF0000']]
print(hashNo.set('white', '#FFFFFF')) # [['red', '#FF0000'], ['red', '#FF0000'], ['white', '#FFFFFF']]
print(hashNo.get('red')) 			 # #red
print(hashNo.get('meme')) 			 # None
print('******') 
print(hashNo.keys()) 				 # ['red', 'white']
print(hashNo.values()) 				 # ['#FF0000', '#FFFFFF']