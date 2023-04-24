import pytest
from lib.drive_a_single_function import *

def test_returns_text():
    result = count_words("hello")
    assert result == 1

def test_returns_number_of_words():
    result = count_words("Hello how are you?")
    assert result == 4

# def test_empty_string():
#     result = count_words(None)
#     with pytest.raises(Exception) as e:
#         result == None
#     err_msg = str(e.value)
#     assert err_msg == "Empty String"

