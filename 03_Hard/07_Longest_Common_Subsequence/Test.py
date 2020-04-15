from Longest_Common_Subsequence import longestCommonSubsequence
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(longestCommonSubsequence("", ""), [])
	
	def test_case_2(self):
		self.assertEqual(longestCommonSubsequence("", "ABCDEFG"), [])
	
	def test_case_3(self):
		self.assertEqual(longestCommonSubsequence("ABCDEFG", ""), [])
	
	def test_case_4(self):
		self.assertEqual(longestCommonSubsequence("ABCDEFG", "ABCDEFG"), ["A", "B", "C", "D", "E", "F", "G"])
	
	def test_case_5(self):
		self.assertEqual(longestCommonSubsequence("ABCDEFG", "APPLES"), ["A", "E"])
	
	def test_case_6(self):
		self.assertEqual(longestCommonSubsequence("clement", "antoine"), ["n", "t"])
	
	def test_case_7(self):
		self.assertEqual(longestCommonSubsequence("ZXVVYZW", "XKYKZPW"), ["X", "Y", "Z", "W"])
	
	def test_case_8(self):
		self.assertEqual(longestCommonSubsequence("8111111111111111142", "222222222822222222222222222222433333333332"), ["8", "4", "2"])
	
	def test_case_9(self):
		self.assertEqual(longestCommonSubsequence("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAG"), ["C", "D", "E", "G", "H", "J", "K", "L", "W"])
	
	def test_case_10(self):
		self.assertEqual(longestCommonSubsequence("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAGTUV"), ["C", "D", "E", "G", "H", "J", "K", "L", "T", "U", "V"])
	

if __name__ == "__main__":
	unittest.main()

