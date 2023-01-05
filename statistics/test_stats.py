from statistics import median
import unittest
from stats import AvgCalc

# Input array
list = [13, 21, 21, 40, 42, 48, 55, 72]
avgCalc = AvgCalc(list)


class Test_Stats(unittest.TestCase):
    def test_mean(self):
        mean = avgCalc.mean()
        self.assertEqual(mean, 39, "Mean should be = 8")

    def test_median(self):
        median = avgCalc.median()
        self.assertEqual(median, 41, "Median should be = 41")


if __name__ == '__main__':
    unittest.main()
