import pytest

@pytest.mark.regression
def test_sum():
    a = 10
    b = 5
    assert 10+5 == 15

@pytest.mark.regression
def test_sub():
    a = 10
    b = 5
    assert 10-5 == 15