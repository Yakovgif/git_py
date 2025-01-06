import pytest
from tests.string_utils import reverse_string,is_palindrom


@pytest.mark.parametrize('param, expected', [('hello','olleh'),('python','lohtyp')])
def test_reverse_string(param, expected):
    assert reverse_string(param) == expected
    # assert reverse_string('python') == 'lohtyp'

def test_is_palindrom():
    assert is_palindrom('Hello,world') is False


