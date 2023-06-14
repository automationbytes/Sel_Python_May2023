import pytest

@pytest.mark.parametrize("a,b,sum",[(1,2,3),(5,5,10),(9,2,10)])
def test_add(a,b,sum):
    assert a+b == sum