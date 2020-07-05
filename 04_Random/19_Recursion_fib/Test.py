import unittest
from fib import fib

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(fib(4), 3)

	def test_case_2(self):
		self.assertEqual(fib(10), 55)

	def test_case_3(self):
		self.assertEqual(fib(28), 317811)

	def test_case_4(self):
		self.assertEqual(fib(35), 9227465)

if __name__=='__main__':
	unittest.main()