from example  import is_valid
import pytest

@pytest.mark.parameterize('url', [
    'http://www.google.com',
    'https://www.google.com'
])
def test_should_return_true_if_url_is_valid():
    assert is_valid(url) is True

@pytest.mark.parameterize('url',[
    'http://www.google.com',
    'https://www.google.com'
])

def test_should_return_false_if_url_is_invalid(url):

    assert is_valid(url) is False
