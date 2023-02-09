import pytest
import b1 as f1

@pytest.mark.parametrize("test_input,expected", [(7, 7), (5, 6), (41, 42)])
def test_eval(test_input, expected):
    assert f1.fun(test_input) == expected