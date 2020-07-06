import unittest
from isPalindrome import isPalindrome

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(isPalindrome('awesome'), False)

	def test_case_2(self):
		self.assertEqual(isPalindrome('foobar'), False)

	def test_case_3(self):
		self.assertEqual(isPalindrome('tacocat'), True)

	def test_case_4(self):
		self.assertEqual(isPalindrome('amanaplanaccanalpanama'), True)

	def test_case_5(self):
		self.assertEqual(isPalindrome('amanaplanacanalpanamonium'), False)

	def test_case_6(self):
		self.assertEqual(isPalindrome(''), False)

	def test_case_6(self):
		self.assertEqual(isPalindrome('aa'), True)

if __name__=='__main__':
	unittest.main()