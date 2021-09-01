import unittest

def add(la, lb):
	return la+lb

class TestSum(unittest.TestCase):
	vala = 100
	valb = 200

	def test_gen_a(self):
		self.assertAlmostEqual(33/7, 4.7142857142)

	def test_sum_a(self):
		self.assertEqual(add(self.vala, self.valb), 300)

	def test_sum_b(self):
		self.assertEqual(sum([20, 20, 30]), 70, "should be 70")

if __name__ == "__main__":
	unittest.main()
