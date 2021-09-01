import unittest

def add(la, lb):
	return la+lb

class TestSum(unittest.TestCase):
	vala = 100
	valb = 200

	@unittest.skipIf(valb > vala, "skip if b > a")
	def test_one(self):
		self.assertEqual(add(self.vala, self.valb), 400)

	@unittest.skipUnless(valb > vala, "dont skip if b > a")
	def test_two(self):
		self.assertEqual(add(self.vala, self.valb), 400)

	@unittest.skip("will look at it later")
	def test_three(self):
		self.assertEqual(add(self.vala, self.valb), 400)

	@unittest.expectedFailure
	def test_four(self):
		self.assertEqual(add(self.vala, self.valb), 400)


if __name__ == "__main__":
	unittest.main()
