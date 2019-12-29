from Nth_Fibonacci import getNthFib
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(getNthFib(1), 0)
	
	def test_case_2(self):
		self.assertEqual(getNthFib(2), 1)
	
	def test_case_3(self):
		self.assertEqual(getNthFib(3), 1)
	
	def test_case_4(self):
		self.assertEqual(getNthFib(4), 2)
	
	def test_case_5(self):
		self.assertEqual(getNthFib(5), 3)
	
	def test_case_6(self):
		self.assertEqual(getNthFib(6), 5)
	
	def test_case_7(self):
		self.assertEqual(getNthFib(7), 8)
	
	def test_case_8(self):
		self.assertEqual(getNthFib(8), 13)
	
	def test_case_9(self):
		self.assertEqual(getNthFib(9), 21)
	
	def test_case_10(self):
		self.assertEqual(getNthFib(10), 34)
	
	def test_case_11(self):
		self.assertEqual(getNthFib(11), 55)
	
	def test_case_12(self):
		self.assertEqual(getNthFib(12), 89)
	
	def test_case_13(self):
		self.assertEqual(getNthFib(13), 144)
	
	def test_case_14(self):
		self.assertEqual(getNthFib(14), 233)
	
	def test_case_15(self):
		self.assertEqual(getNthFib(15), 377)
	
	def test_case_16(self):
		self.assertEqual(getNthFib(16), 610)
	
	def test_case_17(self):
		self.assertEqual(getNthFib(17), 987)
	
	def test_case_18(self):
		self.assertEqual(getNthFib(18), 1597)
	

if __name__ == "__main__":
	unittest.main()

