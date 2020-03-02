from Min_Heap_Construction import MinHeap
import unittest


test1 = MinHeap([2, 3, 1])

test2 = MinHeap([1, 2, 3, 4, 5, 6, 7, 8, 9])

test3 = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
test3.insert(76)
test3.remove()
test3.remove()
test3.insert(87)

test4 = MinHeap([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8])

test5 = MinHeap([-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8])
test5.remove()
test5.insert(-8)
test5.remove()
test5.insert(8)

test6 = MinHeap([427, 787, 222, 996, -359, -614, 246, 230, 107, -706, 568, 9, -246, 12, -764, -212, -484, 603, 934, -848, -646, -991, 661, -32, -348, -474, -439, -56, 507, 736, 635, -171, -215, 564, -710, 710, 565, 892, 970, -755, 55, 821, -3, -153, 240, -160, -610, -583, -27, 131])

test7 = MinHeap([991, -731, -882, 100, 280, -43, 432, 771, -581, 180, -382, -998, 847, 80, -220, 680, 769, -75, -817, 366, 956, 749, 471, 228, -435, -269, 652, -331, -387, -657, -255, 382, -216, -6, -163, -681, 980, 913, -169, 972, -523, 354, 747, 805, 382, -827, -796, 372, 753, 519, 906])
test7.remove()
test7.remove()
test7.remove()
test7.insert(992)

test8 = MinHeap([544, -578, 556, 713, -655, -359, -810, -731, 194, -531, -685, 689, -279, -738, 886, -54, -320, -500, 738, 445, -401, 993, -753, 329, -396, -924, -975, 376, 748, -356, 972, 459, 399, 669, -488, 568, -702, 551, 763, -90, -249, -45, 452, -917, 394, 195, -877, 153, 153, 788, 844, 867, 266, -739, 904, -154, -947, 464, 343, -312, 150, -656, 528, 61, 94, -581])

test9 = MinHeap([-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356, -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490, 995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295, 800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738, -469, -167, -420, -126, -410, 59])
test9.insert(2)
test9.insert(22)
test9.insert(222)
test9.insert(2222)
test9.remove()
test9.remove()
test9.remove()
test9.remove()


class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(test1.heap[0] == min(test1.heap), True)
		for currentIdx in range(len(test1.heap)):
			parentIdx = (currentIdx - 1) // 2
			if parentIdx < 0:
				break
			self.assertEqual(test1.heap[currentIdx] >= test1.heap[parentIdx], True)

	def test_case_2(self):
		self.assertEqual(test2.heap[0] == min(test2.heap), True)
		for currentIdx in range(len(test2.heap)):
			parentIdx = (currentIdx - 1) // 2
			if parentIdx < 0:
				break
			self.assertEqual(test2.heap[currentIdx] >= test2.heap[parentIdx], True)

	def test_case_3(self):
		self.assertEqual(test3.heap[0] == min(test3.heap), True)
		for currentIdx in range(len(test3.heap)):
			parentIdx = (currentIdx - 1) // 2
			if parentIdx < 0:
				break
			self.assertEqual(test3.heap[currentIdx] >= test3.heap[parentIdx], True)

	def test_case_4(self):
		self.assertEqual(test4.heap[0] == min(test4.heap), True)
		for currentIdx in range(len(test4.heap)):
			parentIdx = (currentIdx - 1) // 2
			if parentIdx < 0:
				break
			self.assertEqual(test4.heap[currentIdx] >= test4.heap[parentIdx], True)

	def test_case_5(self):
		self.assertEqual(test5.heap[0] == min(test5.heap), True)
		for currentIdx in range(len(test5.heap)):
			parentIdx = (currentIdx - 1) // 2
			if parentIdx < 0:
				break
			self.assertEqual(test5.heap[currentIdx] >= test5.heap[parentIdx], True)

	def test_case_6(self):
		self.assertEqual(test6.heap[0] == min(test6.heap), True)
		for currentIdx in range(len(test6.heap)):
			parentIdx = (currentIdx - 1) // 2
			if parentIdx < 0:
				break
			self.assertEqual(test6.heap[currentIdx] >= test6.heap[parentIdx], True)

	def test_case_7(self):
		self.assertEqual(test7.heap[0] == min(test7.heap), True)
		for currentIdx in range(len(test7.heap)):
			parentIdx = (currentIdx - 1) // 2
			if parentIdx < 0:
				break
			self.assertEqual(test7.heap[currentIdx] >= test7.heap[parentIdx], True)

	def test_case_8(self):
		self.assertEqual(test8.heap[0] == min(test8.heap), True)
		for currentIdx in range(len(test8.heap)):
			parentIdx = (currentIdx - 1) // 2
			if parentIdx < 0:
				break
			self.assertEqual(test8.heap[currentIdx] >= test8.heap[parentIdx], True)

	def test_case_9(self):
		self.assertEqual(test9.heap[0] == min(test9.heap), True)
		for currentIdx in range(len(test9.heap)):
			parentIdx = (currentIdx - 1) // 2
			if parentIdx < 0:
				break
			self.assertEqual(test9.heap[currentIdx] >= test9.heap[parentIdx], True)


if __name__ == "__main__":
	unittest.main()
