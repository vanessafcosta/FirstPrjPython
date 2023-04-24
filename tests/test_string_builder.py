from lib.string_builder import *

def test_size_string():
    string = StringBuilder()
    string.add("something")
    result = string.size()
    assert result == 9

def test_output_string():
    string = StringBuilder()
    string.add("something")
    result = string.output()
    assert result == "something"

    
# def test_size_string():
#     test_def_string()
#     result = 9
    
