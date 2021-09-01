import unittest
import time
import timeout_decorator

def divide(la, lb):
	return la/lb


class TestSum(unittest.TestCase):
	vala = 100
	valb = 200

	@timeout_decorator.timeout(10)
	def test_two(self):
		for i in range(6, 0, -1):
			print(i, "seconds are left for one")
			time.sleep(1)

	@timeout_decorator.timeout(4)
	def test_three(self):
		for i in range(6, 0, -1):
			print(i, "seconds are left for two")
			time.sleep(1)

if __name__ == "__main__":
	unittest.main()
