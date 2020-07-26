import unittest
from findPair import findPair

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(findPair([6,1,4,10,2,4], 2), True)

	def test_case_2(self):
		self.assertEqual(findPair([8,6,2,4,1,0,2,5,13], 1), True)

	def test_case_3(self):
		self.assertEqual(findPair([4,-2,3,10],-6), True)

	def test_case_4(self):
		self.assertEqual(findPair([6,1,4,10,2,4], 22), False)

	def test_case_5(self):
		self.assertEqual(findPair([], 0), False)

	def test_case_5(self):
		self.assertEqual(findPair([5, 5], 0), True)

	def test_case_5(self):
		self.assertEqual(findPair([-4, 4], -8), True)

	def test_case_5(self):
		self.assertEqual(findPair([-4, 4], 8), True)

	def test_case_5(self):
		self.assertEqual(findPair([1,3,4,6], -2), True)
if __name__ == '__main__':
	unittest.main()