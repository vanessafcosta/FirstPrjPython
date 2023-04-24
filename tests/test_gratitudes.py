from lib.gratitudes import *

def test_gratitudes_format():
    gratitude = Gratitudes()
    gratitude.add("A Job")
    result = gratitude.format()
    assert result == "Be grateful for: A Job"