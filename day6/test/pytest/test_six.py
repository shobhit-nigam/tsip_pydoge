import pytest

@pytest.mark.parametrize("vala, valb, res", [(30, 10, 3), (48, 12, 4), (33, 11, 2)])
def test_div_c(vala, valb, res):
    assert vala/valb == res
