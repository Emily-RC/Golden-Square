from lib.greet import *

def test_greet_with_name():
    result = greet("Sarah")
    assert result == f"Hello, Sarah!"


# def test_add_five_returns_eight_for_three():
#     result = add_five(3)
#     assert result == 8

#     def greet(name):
#     return f"Hello, {name}!"


# def add_five(num):
#     return num + 5