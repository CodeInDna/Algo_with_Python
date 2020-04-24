from Knapsack_Problem import knapsackProblem
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]])
	
	def test_case_2(self):
		self.assertEqual(knapsackProblem([[465, 100], [400, 85], [255, 55], [350, 45], [650, 130], [1000, 190], [455, 100], [100, 25], [1200, 190], [320, 65], [750, 100], [50, 45], [550, 65], [100, 50], [600, 70], [240, 40]], 200), [1500, [3, 12, 14]])
	
	def test_case_3(self):
		self.assertEqual(knapsackProblem([[465, 100], [400, 85], [255, 55], [350, 45], [650, 130], [1000, 190], [455, 100], [100, 25], [1200, 190], [320, 65], [750, 100], [50, 45], [550, 65], [100, 50], [600, 70], [255, 40]], 200), [1505, [7, 12, 14, 15]])
	
	def test_case_4(self):
		self.assertEqual(knapsackProblem([[2, 1], [70, 70], [30, 30], [69, 69], [100, 100]], 100), [101, [0, 2, 3]])
	
	def test_case_5(self):
		self.assertEqual(knapsackProblem([[1, 2], [70, 70], [30, 30], [69, 69], [100, 100]], 100), [100, [1, 2]])
	
	def test_case_6(self):
		self.assertEqual(knapsackProblem([[1, 2], [70, 70], [30, 30], [69, 69], [100, 100]], 0), [0, []])
	

if __name__ == "__main__":
	unittest.main()

