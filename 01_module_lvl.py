import pytest

pytestmark = [
    pytest.mark.parametrize('x', [1, 2, 3])
]


def test_simple_first(x):
    assert x


def test_simple_second(x):
    assert x > 0
