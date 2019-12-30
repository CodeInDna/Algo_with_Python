from Palindrome_Check import isPalindrome
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(isPalindrome("a"), True)
	
	def test_case_2(self):
		self.assertEqual(isPalindrome("ab"), False)
	
	def test_case_3(self):
		self.assertEqual(isPalindrome("aba"), True)
	
	def test_case_4(self):
		self.assertEqual(isPalindrome("abb"), False)
	
	def test_case_5(self):
		self.assertEqual(isPalindrome("abba"), True)
	
	def test_case_6(self):
		self.assertEqual(isPalindrome("abcdcba"), True)
	
	def test_case_7(self):
		self.assertEqual(isPalindrome("abcdefghhgfedcba"), True)
	
	def test_case_8(self):
		self.assertEqual(isPalindrome("abcdefghihgfedcba"), True)
	
	def test_case_9(self):
		self.assertEqual(isPalindrome("abcdefghihgfeddcba"), False)
	

if __name__ == "__main__":
	unittest.main()

