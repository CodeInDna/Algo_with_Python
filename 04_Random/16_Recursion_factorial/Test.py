import unittest
from factorial import factorial

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(factorial(1), 1)

	def test_case_2(self):
		self.assertEqual(factorial(2), 2)

	def test_case_3(self):
		self.assertEqual(factorial(4), 24)

	def test_case_4(self):
		self.assertEqual(factorial(7), 5040)

	def test_case_5(self):
		self.assertEqual(factorial(0), 1)

if __name__=='__main__':
	unittest.main()