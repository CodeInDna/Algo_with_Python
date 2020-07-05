import unittest
from power import power

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(power(2, 0), 1)

	def test_case_2(self):
		self.assertEqual(power(2, 2), 4)

	def test_case_3(self):
		self.assertEqual(power(2, 4), 16)

	def test_case_4(self):
		self.assertEqual(power(6, 5), 7776)

if __name__=='__main__':
	unittest.main()