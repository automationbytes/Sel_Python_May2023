import pytest

@pytest.mark.regression
def test_add():
    print("add method")

@pytest.mark.sanity
def test_sub():
    print("sub method")

@pytest.mark.regression
def test_mul():
    print("mul method")

@pytest.mark.sanity
def test_div():
    print("div method")
