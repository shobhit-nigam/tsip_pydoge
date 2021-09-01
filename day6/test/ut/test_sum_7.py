import unittest

def add(la, lb):
	return la+lb

class TestSum(unittest.TestCase):
	vala = 100
	valb = 200

	@unittest.skipIf(valb > vala, "skip if b > a")
	def test_one(self):
		self.assertEqual(add(self.vala, self.valb), 400)

	def test_two(self):
		self.assertEqual(add(self.vala, self.valb), 400)

if __name__ == "__main__":
	unittest.main()
