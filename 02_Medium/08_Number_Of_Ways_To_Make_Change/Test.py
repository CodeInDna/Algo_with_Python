from Number_Of_Ways_To_Make_Change import numberOfWaysToMakeChange
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(numberOfWaysToMakeChange(0, [2, 3, 4, 7]), 1)
	
	def test_case_2(self):
		self.assertEqual(numberOfWaysToMakeChange(9, [5]), 0)
	
	def test_case_3(self):
		self.assertEqual(numberOfWaysToMakeChange(7, [2, 4]), 0)
	
	def test_case_4(self):
		self.assertEqual(numberOfWaysToMakeChange(6, [1, 5]), 2)
	
	def test_case_5(self):
		self.assertEqual(numberOfWaysToMakeChange(4, [1, 5, 10, 25]), 1)
	
	def test_case_6(self):
		self.assertEqual(numberOfWaysToMakeChange(5, [1, 5, 10, 25]), 2)
	
	def test_case_7(self):
		self.assertEqual(numberOfWaysToMakeChange(10, [1, 5, 10, 25]), 4)
	
	def test_case_8(self):
		self.assertEqual(numberOfWaysToMakeChange(25, [1, 5, 10, 25]), 13)
	
	def test_case_9(self):
		self.assertEqual(numberOfWaysToMakeChange(12, [2, 3, 7]), 4)
	
	def test_case_10(self):
		self.assertEqual(numberOfWaysToMakeChange(7, [2, 3, 4, 7]), 3)
	

if __name__ == "__main__":
	unittest.main()

