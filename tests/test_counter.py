from lib.counter import *

def test_returns_count():
    count = Counter()
    count.add(10)
    result = count.report()
    assert result == "Counted to 10 so far."

def test_returns_error():
    count = Counter()
    count.add(2)
    result = count.report()
    assert result == "Counted to 2 so far."