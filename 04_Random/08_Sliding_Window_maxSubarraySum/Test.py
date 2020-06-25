import unittest
from maxSubarraySum import maxSubarraySum


class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 2), 10)

	def test_case_2(self):
		self.assertEqual(maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 4), 17)

	def test_case_3(self):
		self.assertEqual(maxSubarraySum([4, 2, 1, 6], 1), 6)

	def test_case_4(self):
		self.assertEqual(maxSubarraySum([4, 2, 1, 6, 2], 4), 13)

	def test_case_5(self):
		self.assertEqual(maxSubarraySum([], 4), None)

	def test_case_6(self):
		self.assertEqual(maxSubarraySum([1, 2], 4), None)

	def test_case_7(self):
		self.assertEqual(maxSubarraySum([1, -2, -3, -1, -2, -3], 2), -1)

if __name__=='__main__':
	unittest.main()