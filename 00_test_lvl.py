import pytest


@pytest.mark.parametrize('x', [1, 2, 3])
def test_simple(x):
	assert x == 2
