import unittest
from frequency_counter_digits import sameFrequency

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(sameFrequency(128, 821), True)

	def test_case_2(self):
		self.assertEqual(sameFrequency(22, 2222), False)

	def test_case_3(self):
		self.assertEqual(sameFrequency(3589578, 5879385), True)

	def test_case_4(self):
		self.assertEqual(sameFrequency(34, 14), False)


if __name__ == '__main__':
	unittest.main()