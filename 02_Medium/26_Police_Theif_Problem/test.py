import unittest
from PoliceTheifProblem import catch_the_theif



class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(catch_the_theif(['P', 'T', 'T', 'P', 'T'], 1), 2)

	def test_case_2(self):
		self.assertEqual(catch_the_theif(['T', 'T', 'P', 'P', 'T', 'P'], 2), 3)

	def test_case_3(self):
		self.assertEqual(catch_the_theif(['P', 'T', 'P', 'T', 'T', 'P'], 3), 3)

	def test_case_4(self):
		self.assertEqual(catch_the_theif(['P', 'T', 'P', 'P', 'T', 'P', 'T'], 2), 3)

	def test_case_5(self):
		self.assertEqual(catch_the_theif(['P', 'T', 'P', 'T', 'T', 'P'], 3), 3)


if __name__ == "__main__":
	unittest.main()
