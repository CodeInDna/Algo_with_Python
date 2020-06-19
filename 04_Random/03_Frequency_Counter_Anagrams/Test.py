import unittest
from Anagrams import validAnagrams

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(validAnagrams('anagram', 'nagaram'), True)

	def test_case_2(self):
		self.assertEqual(validAnagrams('', ''), True)

	def test_case_3(self):
		self.assertEqual(validAnagrams('awesome', 'awesom'), False)

	def test_case_4(self):
		self.assertEqual(validAnagrams('aaz', 'zza'), False)

	def test_case_5(self):
		self.assertEqual(validAnagrams('texttwisttime', 'timetwisttext'), True)
if __name__ == '__main__':
	unittest.main()