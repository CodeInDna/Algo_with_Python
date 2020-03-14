from Powerset import powerset
import unittest


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        out = powerset([])
        out = list(map(lambda x: set(x), out))
        self.assertTrue(len(out) == 1)
        self.assertTrue(set([]) in out)

    def test_case_2(self):
        out = powerset([1])
        out = list(map(lambda x: set(x), out))
        self.assertTrue(len(out) == 2)
        self.assertTrue(set([]) in out)
        self.assertTrue(set([1]) in out)

    def test_case_3(self):
        out = powerset([1,2])
        out = list(map(lambda x: set(x), out))
        self.assertTrue(len(out) == 4)
        self.assertTrue(set([]) in out)
        self.assertTrue(set([1]) in out)
        self.assertTrue(set([2]) in out)
        self.assertTrue(set([1,2]) in out)

    def test_case_4(self):
        out = powerset([1,2,3])
        out = list(map(lambda x: set(x), out))
        self.assertTrue(len(out) == 8)
        self.assertTrue(set([]) in out)
        self.assertTrue(set([1]) in out)
        self.assertTrue(set([2]) in out)
        self.assertTrue(set([1,2]) in out)
        self.assertTrue(set([3]) in out)
        self.assertTrue(set([1,3]) in out)
        self.assertTrue(set([2,3]) in out)
        self.assertTrue(set([1,2,3]) in out)

    def test_case_5(self):
        out = powerset([1,2,3,4])
        out = list(map(lambda x: set(x), out))
        self.assertTrue(len(out) == 16)
        self.assertTrue(set([]) in out)
        self.assertTrue(set([1]) in out)
        self.assertTrue(set([2]) in out)
        self.assertTrue(set([1,2]) in out)
        self.assertTrue(set([3]) in out)
        self.assertTrue(set([1,3]) in out)
        self.assertTrue(set([2,3]) in out)
        self.assertTrue(set([1,2,3]) in out)
        self.assertTrue(set([4]) in out)
        self.assertTrue(set([1,4]) in out)
        self.assertTrue(set([2,4]) in out)
        self.assertTrue(set([1,2,4]) in out)
        self.assertTrue(set([3,4]) in out)
        self.assertTrue(set([1,3,4]) in out)
        self.assertTrue(set([2,3,4]) in out)
        self.assertTrue(set([1,2,3,4]) in out)


if __name__ == "__main__":
	unittest.main()
