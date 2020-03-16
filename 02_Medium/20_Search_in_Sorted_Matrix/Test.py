from Search_In_Sorted_Matrix import searchInSortedMatrix
import unittest


matrix = [
	[1, 4, 7, 12, 15, 1000],
	[2, 5, 19, 31, 32, 1001],
	[3, 8, 24, 33, 35, 1002],
	[40, 41, 42, 44, 45, 1003],
	[99, 100, 103, 106, 128, 1004],
]


class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(searchInSortedMatrix(matrix, 1), [0, 0])

	def test_case_2(self):
		self.assertEqual(searchInSortedMatrix(matrix, 2), [1, 0])

	def test_case_3(self):
		self.assertEqual(searchInSortedMatrix(matrix, 4), [0, 1])

	def test_case_4(self):
		self.assertEqual(searchInSortedMatrix(matrix, 15), [0, 4])

	def test_case_5(self):
		self.assertEqual(searchInSortedMatrix(matrix, 12), [0, 3])

	def test_case_6(self):
		self.assertEqual(searchInSortedMatrix(matrix, 32), [1, 4])

	def test_case_7(self):
		self.assertEqual(searchInSortedMatrix(matrix, 99), [4, 0])

	def test_case_8(self):
		self.assertEqual(searchInSortedMatrix(matrix, 100), [4, 1])

	def test_case_9(self):
		self.assertEqual(searchInSortedMatrix(matrix, 40), [3, 0])

	def test_case_10(self):
		self.assertEqual(searchInSortedMatrix(matrix, 128), [4, 4])

	def test_case_11(self):
		self.assertEqual(searchInSortedMatrix(matrix, 106), [4, 3])

	def test_case_12(self):
		self.assertEqual(searchInSortedMatrix(matrix, 45), [3, 4])

	def test_case_13(self):
		self.assertEqual(searchInSortedMatrix(matrix, 24), [2, 2])

	def test_case_14(self):
		self.assertEqual(searchInSortedMatrix(matrix, 44), [3, 3])

	def test_case_15(self):
		self.assertEqual(searchInSortedMatrix(matrix, 43), [-1, -1])

	def test_case_16(self):
		self.assertEqual(searchInSortedMatrix(matrix, -1), [-1, -1])

	def test_case_17(self):
		self.assertEqual(searchInSortedMatrix(matrix, 1000), [0, 5])

	def test_case_18(self):
		self.assertEqual(searchInSortedMatrix(matrix, 1004), [4, 5])


if __name__ == "__main__":
	unittest.main()
