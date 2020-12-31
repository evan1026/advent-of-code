import unittest
from parameterized import parameterized
import importlib

answers = [['01', '1', 211899],
           ['01', '2', 275765682],
           ['02', '1', 447],
           ['02', '2', 249],
           ['03', '1', 156],
           ['03', '2', 3521829480],
           ['04', '1', 202],
           ['04', '2', 137],
           ['05', '1', 864],
           ['05', '2', 739],
           ['06', '1', 6662],
           ['06', '2', 3382],
           ['07', '1', 101],
           ['07', '2', 108636],
           ['08', '1', 1553],
           ['08', '2', 1877],
           ['09', '1', 1124361034],
           ['09', '2', 129444555],
           ['10', '1', 2244],
           ['10', '2', 3947645370368],
           ['11', '1', 2329],
           ['11', '2', 2138],
           ['12', '1', 590],
           ['12', '2', 42013]]

class TestAoC(unittest.TestCase):

  @parameterized.expand(answers)
  def test(self, prob, part, answer):
    prob_module = importlib.import_module('prob%s_part%s' % (prob, part))
    self.assertEqual(prob_module.run(), answer)


if  __name__ == '__main__':
  unittest.main()
