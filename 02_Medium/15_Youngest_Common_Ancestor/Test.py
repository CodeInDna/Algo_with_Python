from Youngest_Common_Ancestors import getYoungestCommonAncestor
import unittest


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def addAsAncestor(self, descendants):
        for descendant in descendants:
            descendant.ancestor = self

ancestralTrees = {}
ALPHABET = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for letter in ALPHABET:
    ancestralTrees[letter] = AncestralTree(letter)
ancestralTrees['A'].addAsAncestor([
    ancestralTrees['B'],
    ancestralTrees['C'],
    ancestralTrees['D'],
    ancestralTrees['E'],
    ancestralTrees['F'],
])
ancestralTrees['B'].addAsAncestor([
    ancestralTrees['G'],
    ancestralTrees['H'],
    ancestralTrees['I'],
])
ancestralTrees['C'].addAsAncestor([
    ancestralTrees['J'],
])
ancestralTrees['D'].addAsAncestor([
    ancestralTrees['K'],
    ancestralTrees['L'],
])
ancestralTrees['F'].addAsAncestor([
    ancestralTrees['M'],
    ancestralTrees['N'],
])
ancestralTrees['H'].addAsAncestor([
    ancestralTrees['O'],
    ancestralTrees['P'],
    ancestralTrees['Q'],
    ancestralTrees['R'],
])
ancestralTrees['K'].addAsAncestor([
    ancestralTrees['S'],
])
ancestralTrees['P'].addAsAncestor([
    ancestralTrees['T'],
    ancestralTrees['U'],
])
ancestralTrees['R'].addAsAncestor([
    ancestralTrees['V'],
])
ancestralTrees['V'].addAsAncestor([
    ancestralTrees['W'],
    ancestralTrees['X'],
    ancestralTrees['Y'],
])
ancestralTrees['X'].addAsAncestor([
    ancestralTrees['Z'],
])


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['A'], ancestralTrees['B'])
        self.assertTrue(yca == ancestralTrees['A'])

    def test_case_2(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['B'], ancestralTrees['F'])
        self.assertTrue(yca == ancestralTrees['A'])

    def test_case_3(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['G'], ancestralTrees['M'])
        self.assertTrue(yca == ancestralTrees['A'])

    def test_case_4(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['U'], ancestralTrees['S'])
        self.assertTrue(yca == ancestralTrees['A'])

    def test_case_5(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['Z'], ancestralTrees['M'])
        self.assertTrue(yca == ancestralTrees['A'])

    def test_case_6(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['O'], ancestralTrees['I'])
        self.assertTrue(yca == ancestralTrees['B'])

    def test_case_7(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['T'], ancestralTrees['Z'])
        self.assertTrue(yca == ancestralTrees['H'])

    def test_case_8(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['T'], ancestralTrees['V'])
        self.assertTrue(yca == ancestralTrees['H'])

    def test_case_9(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['T'], ancestralTrees['H'])
        self.assertTrue(yca == ancestralTrees['H'])

    def test_case_10(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['W'], ancestralTrees['V'])
        self.assertTrue(yca == ancestralTrees['V'])

    def test_case_11(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['Z'], ancestralTrees['B'])
        self.assertTrue(yca == ancestralTrees['B'])

    def test_case_12(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['Q'], ancestralTrees['W'])
        self.assertTrue(yca == ancestralTrees['H'])

    def test_case_13(self):
        yca = getYoungestCommonAncestor(ancestralTrees['A'], ancestralTrees['A'], ancestralTrees['Z'])
        self.assertTrue(yca == ancestralTrees['A'])


if __name__ == "__main__":
	unittest.main()
