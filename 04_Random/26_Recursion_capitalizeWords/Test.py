import unittest
from capitalizeWords import capitalizeWords

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(capitalizeWords(['taco', 'banana', 'car']), ['TACO', 'BANANA', 'CAR'])

	def test_case_2(self):
		self.assertEqual(capitalizeWords(['taco']), ['TACO'])

	def test_case_3(self):
		self.assertEqual(capitalizeWords([]), [])

	def test_case_4(self):
		self.assertEqual(capitalizeWords(['taco', 'banana', 'car', 'mango', 'apple']), ['TACO', 'BANANA', 'CAR', 'MANGO', 'APPLE'])

if __name__=='__main__':
	unittest.main()