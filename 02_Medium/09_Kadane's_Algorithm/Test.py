from Kadanes_Algorithm import kadanesAlgorithm
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(kadanesAlgorithm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
	
	def test_case_2(self):
		self.assertEqual(kadanesAlgorithm([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -1)
	
	def test_case_3(self):
		self.assertEqual(kadanesAlgorithm([-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]), -1)
	
	def test_case_4(self):
		self.assertEqual(kadanesAlgorithm([1, 2, 3, 4, 5, 6, -20, 7, 8, 9, 10]), 35)
	
	def test_case_5(self):
		self.assertEqual(kadanesAlgorithm([1, 2, 3, 4, 5, 6, -22, 7, 8, 9, 10]), 34)
	
	def test_case_6(self):
		self.assertEqual(kadanesAlgorithm([1, 2, -4, 3, 5, -9, 8, 1, 2]), 11)
	
	def test_case_7(self):
		self.assertEqual(kadanesAlgorithm([3, 4, -6, 7, 8]), 16)
	
	def test_case_8(self):
		self.assertEqual(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 19)
	
	def test_case_9(self):
		self.assertEqual(kadanesAlgorithm([8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]), 23)
	
	def test_case_10(self):
		self.assertEqual(kadanesAlgorithm([8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 6]), 24)
	
	def test_case_11(self):
		self.assertEqual(kadanesAlgorithm([8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6]), 22)
	
	def test_case_12(self):
		self.assertEqual(kadanesAlgorithm([8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6, 20, -23, 15, 1, -3, 4]), 35)
	
	def test_case_13(self):
		self.assertEqual(kadanesAlgorithm([100, 8, 5, -9, 1, 3, -2, 3, 4, 7, 2, -18, 6, 3, 1, -5, 6, 20, -23, 15, 1, -3, 4]), 135)
	

if __name__ == "__main__":
	unittest.main()
