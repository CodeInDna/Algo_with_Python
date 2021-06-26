from Multi_String_Search import multiStringSearch
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(multiStringSearch("this is a big string", ["this", "yo", "is", "a", "bigger", "string", "kappa"]), [True, False, True, True, False, True, False])

	def test_case_2(self):
		self.assertEqual(multiStringSearch("Mary goes to the shopping center every week.", ["to", "Mary", "centers", "shop", "shopping", "string", "kappa"]), [True, True, False, True, True, False, False])

	def test_case_3(self):
		self.assertEqual(multiStringSearch("adcb akfkw afnmc fkadn vkaca jdaf dacb cdba cbda", ["abcd", "acbd", "adbc", "dabc", "cbda", "cabd", "cdab"]), [False, False, False, False, True, False, False])

	def test_case_4(self):
		self.assertEqual(multiStringSearch("test testing testings tests testers test-takers", ["tests", "testatk", "testiing", "trsatii", "test-taker", "test"]), [True, False, False, False, True, True])

	def test_case_5(self):
		self.assertEqual(multiStringSearch("ndbajwhfawkjljkfaopwdlaawjk dawkj awjkawkfjhkawk ahjwkjad jadfljawd", ["abc", "akwbc", "awbc", "abafac", "ajjfbc", "abac", "jadfl"]), [False, False, False, False, False, False, True])

	def test_case_6(self):
		self.assertEqual(multiStringSearch("ndbajwhfawkjljkfaopwdlaawjk dawkj awjkawkfjhkawk ahjwkjad jadfljawd", ["abc", "akwbc", "awbc", "abafac", "ajjfbc", "abac", "jadfl"]), [False, False, False, False, False, False, True])

	def test_case_7(self):
		self.assertEqual(multiStringSearch("Is this particular test going to pass or is it going to fail? That is the question.", ["that", "the", "questions", "goes", "mountain", "passes", "passed", "going", "is"]), [False, True, False, False, False, False, False, True, True])

	def test_case_8(self):
		self.assertEqual(multiStringSearch("Everything in this test should fail.", ["everything", "inn", "that", "testers", "shall", "failure"]), [False, False, False, False, False, False])


if __name__ == "__main__":
	unittest.main()

