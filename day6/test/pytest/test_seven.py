import pytest
import time

def test_two():
	for i in range(6, 0, -1):
		print(i, "seconds are left for one")
		time.sleep(1)

def test_three():
	for i in range(6, 0, -1):
		print(i, "seconds are left for two")
		time.sleep(1)
