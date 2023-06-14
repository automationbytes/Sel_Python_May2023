import pytest

@pytest.mark.skip("Skipping")
def test_a1():
    print("test1")

@pytest.mark.xfail
def test_a2():
    print("test12")
