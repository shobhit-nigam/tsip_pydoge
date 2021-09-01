import pytest

def test_floor_b():
    vala = 30
    valb = 40
    assert valb//vala == 1

def test_div_c(funca):
    vala = 30
    valb = 40
    assert valb/funca == 1

@pytest.fixture
def funca():
    print("will run first")
    return 40

def test_mul_d():
    vala = 30
    valb = 40
    assert valb*vala == 1200
