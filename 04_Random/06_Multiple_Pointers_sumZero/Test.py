import unittest
from sumZero import sumZero

class TestProgram(unittest.TestCase):

	def test_case1(self):
		self.assertEqual(sumZero([-3, -2, -1, 0, 1, 2, 3]), [-3, 3])

	def test_case2(self):
		self.assertEqual(sumZero([-2, 0, 1, 3]), None)

	def test_case3(self):
		self.assertEqual(sumZero([1, 2, 3]), None)

	def test_case4(self):
		self.assertEqual(sumZero([-101, -50, -20, 1, 20, 80, 52, 100]), [-20, 20])

if __name__ == '__main__':
	unittest.main()