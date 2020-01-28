from Lavanshtein_Distance import levenshteinDistance
import unittest


class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(levenshteinDistance("", ""), 0)

	def test_case_2(self):
		self.assertEqual(levenshteinDistance("", "abc"), 3)

	def test_case_3(self):
		self.assertEqual(levenshteinDistance("abc", "abc"), 0)

	def test_case_4(self):
		self.assertEqual(levenshteinDistance("abc", "abx"), 1)

	def test_case_5(self):
		self.assertEqual(levenshteinDistance("abc", "abcx"), 1)

	def test_case_6(self):
		self.assertEqual(levenshteinDistance("abc", "yabcx"), 2)

	def test_case_7(self):
		self.assertEqual(levenshteinDistance("algoexpert", "algozexpert"), 1)

	def test_case_8(self):
		self.assertEqual(levenshteinDistance("abcdefghij", "1234567890"), 10)

	def test_case_9(self):
		self.assertEqual(levenshteinDistance("abcdefghij", "a234567890"), 9)

	def test_case_10(self):
		self.assertEqual(levenshteinDistance("biting", "mitten"), 4)

	def test_case_11(self):
		self.assertEqual(levenshteinDistance("cereal", "saturday"), 6)

	def test_case_12(self):
		self.assertEqual(levenshteinDistance("cereal", "saturdzz"), 7)

	def test_case_13(self):
		self.assertEqual(levenshteinDistance("abbbbbbbbb", "bbbbbbbbba"), 2)

	def test_case_14(self):
		self.assertEqual(levenshteinDistance("abc", "yabd"), 2)

	def test_case_15(self):
		self.assertEqual(levenshteinDistance("xabc", "abcx"), 2)


if __name__ == "__main__":
	unittest.main()
