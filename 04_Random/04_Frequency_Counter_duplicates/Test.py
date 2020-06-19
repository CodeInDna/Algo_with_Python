import unittest
from duplicates import areThereDuplicates

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(areThereDuplicates(1, 2, 2), True)

	def test_case_2(self):
		self.assertEqual(areThereDuplicates(1, 2, 3), False)

	def test_case_3(self):
		self.assertEqual(areThereDuplicates('a', 'b', 'a'), True)

	def test_case_4(self):
		self.assertEqual(areThereDuplicates('a', 'b', 'c'), False)


if __name__ == '__main__':
	unittest.main()