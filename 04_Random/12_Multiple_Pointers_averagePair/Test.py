import unittest
from averagePair import averagePair


class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(averagePair([1,2,3], 2.5), True)

	def test_case_2(self):
		self.assertEqual(averagePair([1,3,3,5,6,7,10,12,19], 8), True)

	def test_case_3(self):
		self.assertEqual(averagePair([-1,0,3,4,5,6], 4.1), False)

	def test_case_4(self):
		self.assertEqual(averagePair([], 4), False)

if __name__=='__main__':
	unittest.main()