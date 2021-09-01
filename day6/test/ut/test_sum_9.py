import unittest

def divide(la, lb):
	return la/lb

class TestSum(unittest.TestCase):
	vala = 100
	valb = 200

	def test_one(self):
		self.assertRaises(ZeroDivisionError, divide, self.vala, self.valb)

	def test_two(self):
		self.assertRaises(ZeroDivisionError, divide, 10, 0)

if __name__ == "__main__":
	unittest.main()
