import unittest
from findLongestSubstring import findLongestSubstring


class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(findLongestSubstring(''), 0)

	def test_case_2(self):
		self.assertEqual(findLongestSubstring('rithmschool'), 7)

	def test_case_3(self):
		self.assertEqual(findLongestSubstring('thisisawesome'), 6)

	def test_case_4(self):
		self.assertEqual(findLongestSubstring('thecatinthehat'), 7)

	def test_case_5(self):
		self.assertEqual(findLongestSubstring('bbbbbbb'), 1)

	def test_case_6(self):
		self.assertEqual(findLongestSubstring('longestsubstring'), 8)

	def test_case_7(self):
		self.assertEqual(findLongestSubstring('thisishowwedoit'), 6)

if __name__=='__main__':
	unittest.main()