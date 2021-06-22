# Add, edit, or remove tests in this file.
# Treat it as your playground!

from Longest_Substring_Without_Duplication import longestSubstringWithoutDuplication
import unittest

class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(longestSubstringWithoutDuplication("a"), "a")
	
	def test_case_2(self):
		self.assertEqual(longestSubstringWithoutDuplication("abc"), "abc")
	
	def test_case_3(self):
		self.assertEqual(longestSubstringWithoutDuplication("abcb"), "abc")
	
	def test_case_4(self):
		self.assertEqual(longestSubstringWithoutDuplication("abcdeabcdefc"), "abcdef")
	
	def test_case_5(self):
		self.assertEqual(longestSubstringWithoutDuplication("abccdeaabbcddef"), "cdea")
	
	def test_case_6(self):
		self.assertEqual(longestSubstringWithoutDuplication("abacacacaaabacaaaeaaafa"), "bac")
	
	def test_case_7(self):
		self.assertEqual(longestSubstringWithoutDuplication("abcdabcef"), "dabcef")
	
	def test_case_8(self):
		self.assertEqual(longestSubstringWithoutDuplication("abcbde"), "cbde")
	
	def test_case_9(self):
		self.assertEqual(longestSubstringWithoutDuplication("clementisacap"), "mentisac")
	
	def test_case_10(self):
		self.assertEqual(longestSubstringWithoutDuplication("clementisanarm"), "mentisa")
	

if __name__ == "__main__":
	unittest.main()

