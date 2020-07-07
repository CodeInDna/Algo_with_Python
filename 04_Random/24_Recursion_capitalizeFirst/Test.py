import unittest
from capitalizeFirst import capitalizeFirst

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(capitalizeFirst(['taco', 'banana', 'car']), ['Taco', 'Banana', 'Car'])

	def test_case_2(self):
		self.assertEqual(capitalizeFirst(['taco']), ['Taco'])

	def test_case_3(self):
		self.assertEqual(capitalizeFirst([]), [])

	def test_case_4(self):
		self.assertEqual(capitalizeFirst(['taco', 'banana', 'car', 'mango', 'apple']), ['Taco', 'Banana', 'Car', 'Mango', 'Apple'])

if __name__=='__main__':
	unittest.main()