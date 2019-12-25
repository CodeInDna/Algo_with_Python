
import unittest
from Depth_First_Search import depth_first_search

class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(depth_first_search([]), ["A", "B", "D", "C"])

	def test_case_2(self):
		self.assertEqual(depth_first_search([]), ["A", "B", "C", "F", "D", "E"])

	def test_case_3(self):
		self.assertEqual(depth_first_search([]), ["A", "B", "C", "D", "F", "E"])

	def test_case_4(self):
		self.assertEqual(depth_first_search([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])

	def test_case_5(self):
		self.assertEqual(depth_first_search([]), ["A", "B", "E", "Q", "R", "F", "I", "J", "O", "C", "P", "D", "G", "K", "H", "L", "M", "S", "W", "X", "Y", "Z", "T", "U", "V"])


if __name__ == "__main__":
	unittest.main()
