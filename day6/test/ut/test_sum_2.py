import unittest

class TestSum(unittest.TestCase):
	def test_sum_a(self):
		self.assertEqual(sum([10, 20, 30]), 60, "should be 60")

	def test_sum_b(self):
		self.assertEqual(sum([20, 20, 30]), 70, "should be 70")

if __name__ == "__main__":
	unittest.main()
