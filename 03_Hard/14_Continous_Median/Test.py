from Continous_Median import *
import unittest


test = ContinuousMedianHandler()


class TestProgram(unittest.TestCase):

	def test_case_1(self):
		test.insert(5)
		self.assertEqual(test.getMedian(), 5)
		test.insert(10)
		self.assertEqual(test.getMedian(), 7.5)

	def test_case_2(self):
		test.insert(100)
		self.assertEqual(test.getMedian(), 10)
		test.insert(200)
		self.assertEqual(test.getMedian(), 55)

	def test_case_3(self):
		test.insert(6)
		self.assertEqual(test.getMedian(), 10)
		test.insert(13)
		self.assertEqual(test.getMedian(), 11.5)

	def test_case_4(self):
		test.insert(14)
		self.assertEqual(test.getMedian(), 13)
		test.insert(50)
		self.assertEqual(test.getMedian(), 13.5)

	def test_case_5(self):
		test.insert(51)
		self.assertEqual(test.getMedian(), 14)
		test.insert(52)
		self.assertEqual(test.getMedian(), 32)

	def test_case_6(self):
		test.insert(1000)
		self.assertEqual(test.getMedian(), 50)
		test.insert(10000)
		self.assertEqual(test.getMedian(), 50.5)

	def test_case_7(self):
		test.insert(10001)
		self.assertEqual(test.getMedian(), 51)
		test.insert(10002)
		self.assertEqual(test.getMedian(), 51.5)

	def test_case_8(self):
		test.insert(10003)
		self.assertEqual(test.getMedian(), 52)
		test.insert(10004)
		self.assertEqual(test.getMedian(), 76)

	def test_case_9(self):
		test.insert(75)
		self.assertEqual(test.getMedian(), 75)
		test.insert(80)
		self.assertEqual(test.getMedian(), 77.5)


if __name__ == "__main__":
	unittest.main()
