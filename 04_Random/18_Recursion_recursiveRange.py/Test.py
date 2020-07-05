import unittest
from recursiveRange import recursiveRange

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(recursiveRange(6), 21)

	def test_case_2(self):
		self.assertEqual(recursiveRange(10), 55)

	def test_case_3(self):
		self.assertEqual(recursiveRange(28), 120)

	def test_case_4(self):
		self.assertEqual(recursiveRange(1), 1)

if __name__=='__main__':
	unittest.main()