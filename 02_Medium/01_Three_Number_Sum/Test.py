from Three_Number_Sum import threeNumberSum
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(threeNumberSum([1, 2, 3], 6), [[1, 2, 3]])
	
	def test_case_2(self):
		self.assertEqual(threeNumberSum([1, 2, 3], 7), [])
	
	def test_case_3(self):
		self.assertEqual(threeNumberSum([8, 10, -2, 49, 14], 57), [[-2, 10, 49]])
	
	def test_case_4(self):
		self.assertEqual(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
	
	def test_case_5(self):
		self.assertEqual(threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1], 0), [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]])
	
	def test_case_6(self):
		self.assertEqual(threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-1, 0, 1]])
	
	def test_case_7(self):
		self.assertEqual(threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-5, -1, 6], [-5, 0, 5], [-5, 2, 3], [-1, 0, 1]])
	
	def test_case_8(self):
		self.assertEqual(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18), [[1, 2, 15], [1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]])
	
	def test_case_9(self):
		self.assertEqual(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32), [[8, 9, 15]])
	
	def test_case_10(self):
		self.assertEqual(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33), [])
	
	def test_case_11(self):
		self.assertEqual(threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 5), [])
	

if __name__ == "__main__":
	unittest.main()

