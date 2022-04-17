import pytest

pytestmark = [
    pytest.mark.parametrize('x', [1, 2, 3])
]


class TestAll:

    pytestmark = [
        pytest.mark.parametrize('x', [4, 5, 6])
    ]

    @pytest.mark.parametrize('x', [7, 8, 9])
    def test_simple(self, x):
        assert x
