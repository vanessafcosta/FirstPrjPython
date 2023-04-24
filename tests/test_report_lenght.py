from lib.report_lenght import *

def test_report_lenght():
    result = report_length("word")
    assert result == "This string was 4 characters long."