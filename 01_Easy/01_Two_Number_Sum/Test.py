import unittest
from Two_Number_Sum import two_number_sum

class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(two_number_sum([4, 6], 10), [4, 6])
	
	def test_case_2(self):
		self.assertEqual(two_number_sum([4, 6, 1], 5), [1, 4])
	
	def test_case_3(self):
		self.assertEqual(two_number_sum([4, 6, 1, -3], 3), [-3, 6])
	
	def test_case_4(self):
		self.assertEqual(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10), [-1, 11])
	
	def test_case_5(self):
		self.assertEqual(two_number_sum([1, 2, 3, 4, 8, 9], 17), [8, 9])
	
	def test_case_6(self):
		self.assertEqual(two_number_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18), [3, 15])
	
	def test_case_7(self):
		self.assertEqual(two_number_sum([-7, -5, -3, -1, 0, 1, 3, 5, 7], -5), [-5, 0])
	
	def test_case_8(self):
		self.assertEqual(two_number_sum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163), [-47, 210])
	
	def test_case_9(self):
		self.assertEqual(two_number_sum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164), [])
	
	def test_case_10(self):
		self.assertEqual(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 15), [])
	

if __name__ == "__main__":
	unittest.main()

