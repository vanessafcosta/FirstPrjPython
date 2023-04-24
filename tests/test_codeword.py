from lib.check_codework import *

def test_codeword1():
    result = check_codeword("horse")
    assert result == "Correct! Come in."


def test_codeword2(): 
    result = check_codeword("here")
    assert result == "Close, but nope."

def test_codeword3():
    result = check_codeword("ojhyu")
    assert result == "WRONG!"

