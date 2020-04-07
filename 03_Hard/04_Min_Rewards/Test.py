from Min_Rewards import minRewards
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(minRewards([1]), 1)
	
	def test_case_2(self):
		self.assertEqual(minRewards([5, 10]), 3)
	
	def test_case_3(self):
		self.assertEqual(minRewards([10, 5]), 3)

	def test_case_4(self):
		self.assertEqual(minRewards([4, 2, 1, 3]), 8)
	
	def test_case_5(self):
		self.assertEqual(minRewards([0, 4, 2, 1, 3]), 9)
	
	def test_case_6(self):
		self.assertEqual(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)
	
	def test_case_7(self):
		self.assertEqual(minRewards([2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]), 52)
	
	def test_case_8(self):
		self.assertEqual(minRewards([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]), 15)
	
	def test_case_9(self):
		self.assertEqual(minRewards([800, 400, 20, 10, 30, 60, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53]), 93)
	

if __name__ == "__main__":
	unittest.main()
