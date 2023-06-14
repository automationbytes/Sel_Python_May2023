import pytest

@pytest.fixture(scope="function")
def setup():
    print("PreStep")

    yield
    print("Tear down")


def test_a1(setup):
    print("test1")


def test_a2(setup):
    print("test12")
