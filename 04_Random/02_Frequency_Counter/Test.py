import unittest
from frequency_counter import same

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(same([1, 2, 3], [1, 9, 4]), True)

	def test_case_2(self):
		self.assertEqual(same([1, 2], [1, 9, 4]), False)

	def test_case_3(self):
		self.assertEqual(same([1, 2, 3], [1, 9]), False)

	def test_case_4(self):
		self.assertEqual(same([1, 2, 1], [1, 4, 4]), False)

	def test_case_5(self):
		self.assertEqual(same([1, 2, 1], [1, 4, 1]), True)

if __name__ == '__main__':
	unittest.main()