import unittest
from radixSort import radixSort

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(radixSort([8,1,2,3,4,5,6,7]), [1, 2, 3, 4, 5, 6, 7, 8])

	def test_case_2(self):
		self.assertEqual(radixSort([5,4,3,1,2]), [1,2,3,4,5])

	def test_case_3(self):
		self.assertEqual(radixSort([]), [])

	def test_case_4(self):
		self.assertEqual(radixSort([23,345,5467,12,2345,9852,147]), [12, 23, 147, 345, 2345, 5467, 9852])

	def test_case_5(self):
		self.assertEqual(radixSort([123,3245,546337,122,2345,9852,147]), [122, 123, 147, 2345, 3245, 9852, 546337])
		
if __name__=='__main__':
	unittest.main()