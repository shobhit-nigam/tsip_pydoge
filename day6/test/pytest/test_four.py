import pytest

@pytest.mark.floor
def test_floor_a():
    vala = 30
    valb = 40
    assert valb//vala == 1

@pytest.mark.floor
def test_floor_b():
    vala = 30
    valb = 40
    assert valb//vala == 2

@pytest.mark.xyz
def test_div_c():
    vala = 30
    valb = 40
    assert valb/vala == 2

@pytest.mark.xyz
def test_mul_d():
    vala = 30
    valb = 40
    assert valb*vala == 1200
