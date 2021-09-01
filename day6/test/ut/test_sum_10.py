import unittest

def divide(la, lb):
	return la/lb

stra = "a hello heals a wounded hell"
strb = "a hello heals a wounded heel"


class TestSum(unittest.TestCase):
	vala = 100
	valb = 200

	def test_two(self):
		self.assertRegex(stra, "he{2}l")

	def test_two(self):
		self.assertRegex(stra, "he{2l")

if __name__ == "__main__":
	unittest.main()
