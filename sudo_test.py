import unittest
from sudo import *

class sudoTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_FindBlock(self):
        case1 = [[1,1]]
        case2 = [[1,0], [0,1]]
        case3 = [[1,2], [1,0]]
        case4 = [[1,0,0],[1,0,0]]
        self.assertEqual(findBlock(case1), None)
        self.assertEqual(findBlock(case2), (0,1))
        self.assertEqual(findBlock(case3), (1,1))
        self.assertEqual(findBlock(case4), (0,1))
    
    def test_relationRowAndColumn(self):
        locate1 = (0, 0)
        locate2 = (1, 5)
        locate3 = (2, 8)
        locate4 = (3, 2)
        locate5 = (3, 5)
        locate6 = (3, 7)
        locate7 = (8, 1)
        locate8 = (7, 5)
        locate9 = (6, 8)
        self.assertEqual(relationRowAndColumn(locate1), ((0,1,2),(0,1,2)))
        self.assertEqual(relationRowAndColumn(locate2), ((0,1,2),(3,4,5)))
        self.assertEqual(relationRowAndColumn(locate3), ((0,1,2),(6,7,8)))
        self.assertEqual(relationRowAndColumn(locate4), ((3,4,5),(0,1,2)))
        self.assertEqual(relationRowAndColumn(locate5), ((3,4,5),(3,4,5)))
        self.assertEqual(relationRowAndColumn(locate6), ((3,4,5),(6,7,8)))
        self.assertEqual(relationRowAndColumn(locate7), ((6,7,8),(0,1,2)))
        self.assertEqual(relationRowAndColumn(locate8), ((6,7,8),(3,4,5)))
        self.assertEqual(relationRowAndColumn(locate9), ((6,7,8),(6,7,8)))

    def test_findNextBlock(self):
        sudo1 = [[1,2,0,0,1,0],[1,0,4,5,6,0],[3,4,0,1,2,0],[2,4,0,8,5,3],[2,0,9,7,3,0],[4,0,1,3,0,0,0]]
        ori_location = (3,2)
        new_location = findNextBlock(sudo1, ori_location)
        print new_location
        row, column = relationRowAndColumn(ori_location)
        sudo_location = [(x, y) for x in row for y in column]
        self.assertFalse(new_location in sudo_location)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(sudoTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
