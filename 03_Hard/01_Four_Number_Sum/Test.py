from Four_Number_Sum import fourNumberSum
import unittest


def sortAndStringify(array):
    return ",".join(sorted(list(map(lambda x: str(x), array))))


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        output = fourNumberSum([1, 2, 3, 4, 5, 6, 7], 10)
        output = list(map(sortAndStringify, output))
        quadruplets = [
            [1, 2, 3, 4],
        ]
        self.assertTrue(len(output) == 1)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_2(self):
        output = fourNumberSum([7, 6, 4, -1, 1, 2], 16)
        output = list(map(sortAndStringify, output))
        quadruplets = [
            [7, 6, 4, -1],
            [7, 6, 1, 2],
        ]
        self.assertTrue(len(output) == 2)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_3(self):
        output = fourNumberSum([5, -5, -2, 2, 3, -3], 0)
        output = list(map(sortAndStringify, output))
        quadruplets = [
            [5, -5, -2, 2],
            [5, -5, 3, -3],
            [-2, 2, 3, -3],
        ]
        self.assertTrue(len(output) == 3)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_4(self):
        output = fourNumberSum([-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
        output = list(map(sortAndStringify, output))
        quadruplets = [
            [-2, -1, 1, 6],
            [-2, 1, 2, 3],
            [-2, -1, 2, 5],
            [-2, -1, 3, 4],
        ]
        self.assertTrue(len(output) == 4)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_5(self):
        output = fourNumberSum([-1, 22, 18, 4, 7, 11, 2, -5, -3], 30)
        output = list(map(sortAndStringify, output))
        quadruplets = [
            [-1, 22, 7, 2],
            [22, 4, 7, -3],
            [-1, 18, 11, 2],
            [18, 4, 11, -3],
            [22, 11, 2, -5],
        ]
        self.assertTrue(len(output) == 5)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_6(self):
        output = fourNumberSum([-10, -3, -5, 2, 15, -7, 28, -6, 12, 8, 11, 5], 20)
        output = list(map(sortAndStringify, output))
        quadruplets = [
            [-5, 2, 15, 8],
            [-3, 2, -7, 28],
            [-10, -3, 28, 5],
            [-10, 28, -6, 8],
            [-7, 28, -6, 5],
            [-5, 2, 12, 11],
            [-5, 12, 8, 5],
        ]
        self.assertTrue(len(output) == 7)
        for quadruplet in quadruplets:
            self.assertTrue(sortAndStringify(quadruplet) in output)

    def test_case_7(self):
        output = fourNumberSum([1, 2, 3, 4, 5], 100)
        output = list(map(sortAndStringify, output))
        self.assertTrue(len(output) == 0)


if __name__ == "__main__":
	unittest.main()
