# ---------------------------------- PROBLEM 12 (EASY) --------------------------------------#
# Caesar Cipher Encryption
# Given a non-empty string of lowercase letters and a non-negative integer value representing a 
# key, write a function that returns a new string obtained by shifting every letter in the 
# input string by k positions in the alphabet, where k is the key. Note that letters should 
# "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a".

# Sample input: "xyz", 2
# Sample output: "zab"

# ----------------METHOD 01 (Using UNICODE)---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n) 
def caesarCipherEncryptor(string, positions):
	newLetters = []
	newKey = positions % 26
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey))
	return "".join(newLetters)

def getNewLetter(letter, newKey):
	newLetterCode = ord(letter) + newKey		# ord: convert into unicode a: 97, z:122
	return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122) # chr: covert unicode back to character
# ----------------METHOD 01---------------------#


# ----------------METHOD 02---------------------#
# COMPLEXITY = TIME: O(n), SPACE: O(n) 
def caesarCipherEncryptor(string, positions):
	newLetters = []
	newKey = positions % 26
	alphabets = list('abcdefghijklmnopqrstuvwxyz')
	for letter in string:
		newLetters.append(getNewLetter(letter, newKey, alphabets))
	return "".join(newLetters)

def getNewLetter(letter, newKey, alphabets):
	newLetterCode = alphabets.index(letter) + newKey
	return alphabets[newLetterCode] if newLetterCode <= 25 else alphabets[-1 + newLetterCode % 25]
# ----------------METHOD 02---------------------#