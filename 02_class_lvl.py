import pytest


class TestAll:
    pytestmark = [
        pytest.mark.parametrize('x', [1, 2, 3])
    ]

    def test_simple(self, x):
        assert x
