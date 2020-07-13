import unittest
from mergeSort import mergeSort


class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(mergeSort([8, 1, 2, 3, 4, 5, 6, 7]), [1,2,3,4,5,6,7,8])

	def test_case_2(self):
		self.assertEqual(mergeSort([5, 3, 4, 1, 2]), [1,2,3,4,5])

	def test_case_3(self):
		self.assertEqual(mergeSort([]), [])

	def test_case_4(self):
		self.assertEqual(mergeSort([-5, 3, 4, 1, 2]), [-5,1,2,3,4])

	def test_case_5(self):
		self.assertEqual(mergeSort([5, 3, 4, 1, 0, 2]), [0,1,2,3,4,5])
if __name__=='__main__':
	unittest.main()