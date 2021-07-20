from PatternMatcher import patternMatcher
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(patternMatcher("xyxy", "abab"), ["a", "b"])
	
	def test_case_2(self):
		self.assertEqual(patternMatcher("yxyx", "abab"), ["b", "a"])
	
	def test_case_3(self):
		self.assertEqual(patternMatcher("yxx", "yomama"), ["ma", "yo"])
	
	def test_case_4(self):
		self.assertEqual(patternMatcher("xxyxxy", "gogopowerrangergogopowerranger"), ["go", "powerranger"])
	
	def test_case_5(self):
		self.assertEqual(patternMatcher("yyxyyx", "gogopowerrangergogopowerranger"), ["powerranger", "go"])
	
	def test_case_6(self):
		self.assertEqual(patternMatcher("xyxxxyyx", "baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom"), ["baddaddoom", "baddaddoomi"])
	
	def test_case_7(self):
		self.assertEqual(patternMatcher("yxyyyxxy", "baddaddoombaddaddoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom"), ["baddaddoomi", "baddaddoom"])
	
	def test_case_8(self):
		self.assertEqual(patternMatcher("xxyxyy", "testtestwrongtestwrongtest"), [])
	
	def test_case_9(self):
		self.assertEqual(patternMatcher("xyxxxyyx", "baddaddoombaddadoomibaddaddoombaddaddoombaddaddoombaddaddoomibaddaddoomibaddaddoom"), [])
	
	def test_case_10(self):
		self.assertEqual(patternMatcher("xyx", "thisshouldobviouslybewrong"), [])
	
	def test_case_11(self):
		self.assertEqual(patternMatcher("xxxx", "testtesttesttest"), ["test", ""])
	
	def test_case_12(self):
		self.assertEqual(patternMatcher("yyyy", "testtesttesttest"), ["", "test"])
	

if __name__ == "__main__":
	unittest.main()

