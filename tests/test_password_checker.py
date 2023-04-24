from lib.password_checker import *
import pytest

def test_check_password_is_valid():
    password = PasswordChecker()
    result = password.check("pythoncode")
    assert result == True

def test_check_password_is_not_valid():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("python")
    err_msg = str(e.value)
    assert err_msg == "Invalid password, must be 8+ characters."