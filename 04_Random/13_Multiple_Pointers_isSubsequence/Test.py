import unittest
from isSubsequence import isSubsequence


class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(isSubsequence('hello', 'hello world'), True)

	def test_case_2(self):
		self.assertEqual(isSubsequence('sing', 'sting'), True)

	def test_case_3(self):
		self.assertEqual(isSubsequence('abc', 'abracadabra'), True)

	def test_case_4(self):
		self.assertEqual(isSubsequence('abc', 'acb'), False)

if __name__=='__main__':
	unittest.main()