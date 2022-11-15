import PyTest_code as ptc
import pytest

def test_add():
    assert ptc.add(4,5) == 9

def test_sub():
    assert ptc.sub(4,5) == -1

# test all
# python -m pytest "F:\Coursera\Meta-Back-End-Developer-Professional-Certificate\2 - Programming in Python\Week-4\testing\PyTest_test.py"

# test one
# python -m pytest "F:\Coursera\Meta-Back-End-Developer-Professional-Certificate\2 - Programming in Python\Week-4\testing\PyTest_test.py::test_add"

# will accept any boolean value
# + > in not etc