import unittest

import prob01_part1
import prob01_part2
import prob02_part1
import prob02_part2
import prob03_part1
import prob03_part2
import prob04_part1
import prob04_part2
import prob05_part1
import prob05_part2
import prob06_part1
import prob06_part2
import prob07_part1
import prob07_part2
import prob08_part1
import prob08_part2
import prob09_part1
import prob09_part2
import prob10_part1
import prob10_part2

class TestAoC(unittest.TestCase):
  def test_p1p1(self):
    self.assertEqual(prob01_part1.run(), 211899)

  def test_p1p2(self):
    self.assertEqual(prob01_part2.run(), 275765682)

  def test_p2p1(self):
    self.assertEqual(prob02_part1.run(), 447)

  def test_p2p2(self):
    self.assertEqual(prob02_part2.run(), 249)

  def test_p3p1(self):
    self.assertEqual(prob03_part1.run(), 156)

  def test_p3p2(self):
    self.assertEqual(prob03_part2.run(), 3521829480)

  def test_p4p1(self):
    self.assertEqual(prob04_part1.run(), 202)

  def test_p4p2(self):
    self.assertEqual(prob04_part2.run(), 137)

  def test_p5p1(self):
    self.assertEqual(prob05_part1.run(), 864)

  def test_p5p2(self):
    self.assertEqual(prob05_part2.run(), 739)

  def test_p6p1(self):
    self.assertEqual(prob06_part1.run(), 6662)

  def test_p6p2(self):
    self.assertEqual(prob06_part2.run(), 3382)

  def test_p7p1(self):
    self.assertEqual(prob07_part1.run(), 101)

  def test_p7p2(self):
    self.assertEqual(prob07_part2.run(), 108636)

  def test_p8p1(self):
    self.assertEqual(prob08_part1.run(), 1553)

  def test_p8p2(self):
    self.assertEqual(prob08_part2.run(), 1877)

  def test_p9p1(self):
    self.assertEqual(prob09_part1.run(), 1124361034)

  def test_p9p2(self):
    self.assertEqual(prob09_part2.run(), 129444555)

  def test_p10p1(self):
    self.assertEqual(prob10_part1.run(), 2244)

  def test_p10p2(self):
    self.assertEqual(prob10_part2.run(), 3947645370368)


if  __name__ == '__main__':
  unittest.main()
