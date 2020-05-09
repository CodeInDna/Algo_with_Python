from Find_Loops import findLoop
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNthNode(self, n):
        counter = 1
        current = self
        while counter < n:
            current = current.next
            counter += 1
        return current

test1 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test1.getNthNode(10).next = test1.getNthNode(1)

test2 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test2.getNthNode(10).next = test2.getNthNode(2)

test3 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test3.getNthNode(10).next = test3.getNthNode(3)

test4 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test4.getNthNode(10).next = test4.getNthNode(4)

test5 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test5.getNthNode(10).next = test5.getNthNode(5)

test6 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test6.getNthNode(10).next = test6.getNthNode(6)

test7 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test7.getNthNode(10).next = test7.getNthNode(7)

test8 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test8.getNthNode(10).next = test8.getNthNode(8)

test9 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test9.getNthNode(10).next = test9.getNthNode(9)

test10 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test10.getNthNode(10).next = test10.getNthNode(10)

test11 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test11.getNthNode(10).next = test11.getNthNode(0)


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(findLoop(test1), test1.getNthNode(1))

    def test_case_2(self):
        self.assertEqual(findLoop(test2), test2.getNthNode(2))

    def test_case_3(self):
        self.assertEqual(findLoop(test3), test3.getNthNode(3))

    def test_case_4(self):
        self.assertEqual(findLoop(test4), test4.getNthNode(4))

    def test_case_5(self):
        self.assertEqual(findLoop(test5), test5.getNthNode(5))

    def test_case_6(self):
        self.assertEqual(findLoop(test6), test6.getNthNode(6))

    def test_case_7(self):
        self.assertEqual(findLoop(test7), test7.getNthNode(7))

    def test_case_8(self):
        self.assertEqual(findLoop(test8), test8.getNthNode(8))

    def test_case_9(self):
        self.assertEqual(findLoop(test9), test9.getNthNode(9))

    def test_case_10(self):
        self.assertEqual(findLoop(test10), test10.getNthNode(10))

    def test_case_11(self):
        self.assertEqual(findLoop(test11), test11.getNthNode(0))


if __name__ == "__main__":
	unittest.main()
