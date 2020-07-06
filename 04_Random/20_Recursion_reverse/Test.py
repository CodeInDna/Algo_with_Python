import unittest
from reverse import reverse

class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(reverse('awesome'), 'emosewa')

	def test_case_2(self):
		self.assertEqual(reverse('rithmschool'), 'loohcsmhtir')

	def test_case_3(self):
		self.assertEqual(reverse(''), '')

	def test_case_4(self):
		self.assertEqual(reverse('a'), 'a')

if __name__=='__main__':
	unittest.main()