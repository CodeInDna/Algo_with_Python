
import unittest
from Depth_First_Search import Tree

test1 = Tree("A")
test1.addChild("B").addChild("C")
test1.children[0].addChild("D")

test2 = Tree("A")
test2.addChild("B").addChild("C").addChild("D").addChild("E")
test2.children[1].addChild("F")

test3 = Tree("A")
test3.addChild("B")
test3.children[0].addChild("C")
test3.children[0].children[0].addChild("D").addChild("E")
test3.children[0].children[0].children[0].addChild("F")

test4 = Tree("A")
test4.addChild("B").addChild("C").addChild("D")
test4.children[0].addChild("E").addChild("F")
test4.children[2].addChild("G").addChild("H")
test4.children[0].children[1].addChild("I").addChild("J")
test4.children[2].children[0].addChild("K")

test5 = Tree("A")
test5.addChild("B").addChild("C").addChild("D").addChild("L").addChild("M")
test5.children[0].addChild("E").addChild("F").addChild("O")
test5.children[1].addChild("P")
test5.children[2].addChild("G").addChild("H")
test5.children[0].children[0].addChild("Q").addChild("R")
test5.children[0].children[1].addChild("I").addChild("J")
test5.children[2].children[0].addChild("K")
test5.children[4].addChild("S").addChild("T").addChild("U").addChild("V")
test5.children[4].children[0].addChild("W").addChild("X")
test5.children[4].children[0].children[1].addChild("Y").addChild("Z")
class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(test1.depth_first_search([]), ["A", "B", "D", "C"])

	def test_case_2(self):
		self.assertEqual(test2.depth_first_search([]), ["A", "B", "C", "F", "D", "E"])

	def test_case_3(self):
		self.assertEqual(test3.depth_first_search([]), ["A", "B", "C", "D", "F", "E"])

	def test_case_4(self):
		self.assertEqual(test4.depth_first_search([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])

	def test_case_5(self):
		self.assertEqual(test5.depth_first_search([]), ["A", "B", "E", "Q", "R", "F", "I", "J", "O", "C", "P", "D", "G", "K", "H", "L", "M", "S", "W", "X", "Y", "Z", "T", "U", "V"])


if __name__ == "__main__":
	unittest.main()
