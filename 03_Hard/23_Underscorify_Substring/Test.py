from Underscorify_Substring import underscorifySubstring
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(underscorifySubstring("this is a test to see if it works", "test"), "this is a _test_ to see if it works")
	
	def test_case_2(self):
		self.assertEqual(underscorifySubstring("test this is a test to see if it works", "test"), "_test_ this is a _test_ to see if it works")
	
	def test_case_3(self):
		self.assertEqual(underscorifySubstring("testthis is a test to see if it works", "test"), "_test_this is a _test_ to see if it works")
	
	def test_case_4(self):
		self.assertEqual(underscorifySubstring("testthis is a testest to see if testestes it works", "test"), "_test_this is a _testest_ to see if _testest_es it works")
	
	def test_case_5(self):
		self.assertEqual(underscorifySubstring("testthis is a testtest to see if testestest it works", "test"), "_test_this is a _testtest_ to see if _testestest_ it works")
	
	def test_case_6(self):
		self.assertEqual(underscorifySubstring("this is a test to see if it works and test", "test"), "this is a _test_ to see if it works and _test_")
	
	def test_case_7(self):
		self.assertEqual(underscorifySubstring("this is a test to see if it works and test", "bfjawkfja"), "this is a test to see if it works and test")
	
	def test_case_8(self):
		self.assertEqual(underscorifySubstring("ttttttttttttttbtttttctatawtatttttastvb", "ttt"), "_tttttttttttttt_b_ttttt_ctatawta_ttttt_astvb")
	
	def test_case_9(self):
		self.assertEqual(underscorifySubstring("tzttztttz", "ttt"), "tzttz_ttt_z")
	
	def test_case_10(self):
		self.assertEqual(underscorifySubstring("abababababababababababababaababaaabbababaa", "a"), "_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_aa_b_a_b_aaa_bb_a_b_a_b_aa_")
	
	def test_case_11(self):
		self.assertEqual(underscorifySubstring("abcabcabcabcabcabcabcabcabcabcabcabcabcabc", "abc"), "_abcabcabcabcabcabcabcabcabcabcabcabcabcabc_")
	

if __name__ == "__main__":
	unittest.main()

