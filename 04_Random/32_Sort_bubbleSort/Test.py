import unittest
from bubbleSort import bubbleAscSort, bubbleDescSort


class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(bubbleAscSort([8, 1, 2, 3, 4, 5, 6, 7]), [1,2,3,4,5,6,7,8])

	def test_case_2(self):
		self.assertEqual(bubbleAscSort([5, 3, 4, 1, 2]), [1,2,3,4,5])

	def test_case_3(self):
		self.assertEqual(bubbleAscSort([]), [])

	def test_case_4(self):
		self.assertEqual(bubbleDescSort([8, 1, 2, 3, 4, 5, 6, 7]), [8,7,6,5,4,3,2,1])

	def test_case_5(self):
		self.assertEqual(bubbleDescSort([5, 3, 4, 1, 2]), [5,4,3,2,1])

	def test_case_6(self):
		self.assertEqual(bubbleDescSort([]), [])

if __name__=='__main__':
	unittest.main()