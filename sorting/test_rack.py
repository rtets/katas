import unittest
from rack import Rack

class TestRack(unittest.TestCase):
    def test_simple(self):
        unsorted = [10, 40, 11, 59, 0, 1]
        rack = Rack(60)
        for i in range(len(unsorted)):
            rack.add(unsorted[i])
            correct = unsorted[:i+1]
            correct.sort()
            self.assertEqual(correct,rack.balls())

if __name__ == '__main__':
    unittest.main()
