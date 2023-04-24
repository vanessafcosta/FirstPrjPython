import pytest
from lib.present import *

def test_wrap():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap(2)
        present.wrap(3)
    error_msg = str(e.value)
    assert error_msg == "A contents has already been wrapped."
    

def test_unwraps():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_msg = str(e.value)
    assert error_msg == "No contents have been wrapped."