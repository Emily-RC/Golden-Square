from lib.greet import *

def test_greet_with_name():
    result = greet("Sarah")
    assert result == f"Hello, Sarah!"

