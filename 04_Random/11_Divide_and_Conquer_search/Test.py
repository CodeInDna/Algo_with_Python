import unittest
from search import search


class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(search([1, 2, 3, 4, 5, 6], 4), 3)

	def test_case_2(self):
		self.assertEqual(search([1, 2, 3, 4, 5, 6], 6), 5)

	def test_case_3(self):
		self.assertEqual(search([1, 2, 3, 4, 5, 6], 11), -1)

if __name__=='__main__':
	unittest.main()