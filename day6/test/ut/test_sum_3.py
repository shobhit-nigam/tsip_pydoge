import unittest

def add(la, lb):
	return la+lb

class TestSum(unittest.TestCase):
	vala = 100
	valb = 200

	def setUp(self):
		self.vala = self.vala/2
		self.valb = self.valb/2
		print("setting up....\n")

	def tearDown(self):
		print("tearing down")
		self.vala = self.vala*2
		self.valb = self.valb*2

	def test_sum_a(self):
		self.assertEqual(add(self.vala, self.valb), 150)

	def test_sum_b(self):
		self.assertEqual(sum([20, 20, 30]), 70, "should be 70")

if __name__ == "__main__":
	unittest.main()
