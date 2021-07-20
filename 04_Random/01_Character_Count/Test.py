import unittest
from Character_Count import char_count

class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(char_count(""), False)

	def test_case_2(self):
		self.assertEqual(char_count("aaaa"), {"a": 4})

	def test_case_3(self):
		self.assertEqual(char_count("Hello World"), {"h": 1, "e": 1, "l": 3, "o":2, "r": 1, "d":1, "w": 1})

	def test_case_4(self):
		self.assertEqual(char_count("Hello World !"), {"h": 1, "e": 1, "l": 3, "o":2, "r": 1, "d":1, "w": 1})

	def test_case_5(self):
		self.assertEqual(char_count("Hello 912041"), {"h": 1, "e": 1, "l": 2, "o":1, "9": 1, "1": 2, "0":1, "4": 1, "2":1})

	def test_case_6(self):
		self.assertEqual(char_count(91422), False)

if __name__=='__main__':
	unittest.main()