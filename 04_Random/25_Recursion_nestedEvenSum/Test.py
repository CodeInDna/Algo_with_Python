import unittest
from nestedEvenSum import nestedEvenSum

dict1 = {'outer':2,
		'obj':{
			'inner':2,
			'otherobj':{
				'superInner': 2,
				'notANumber':True,
				'alsonotaNumber': "yup"
				}
			}
		}

dict2 = {'a':2,
		'b':{'b':2, 'bb': {'b': 3, 'bb': {'b':2}}},
		'c': {'c': {'c': 2}, 'cc':'ball','ccc':5},
		'd':1,
		'e': {'e': {'e':2}, 'ee':'car'}
		}
class TestProgram(unittest.TestCase):
	def test_case_1(self):
		self.assertEqual(nestedEvenSum(dict1), 6)

	def test_case_2(self):
		self.assertEqual(nestedEvenSum(dict2), 10)

	def test_case_3(self):
		self.assertEqual(nestedEvenSum({'a':2, 'b': 1}), 2)

	def test_case_4(self):
		self.assertEqual(nestedEvenSum({}), 0)

if __name__=='__main__':
	unittest.main()