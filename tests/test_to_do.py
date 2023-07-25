import pytest
from lib.to_do import *

def test_string_contains_to_do():
    result = to_do("Task1 must walk dog #TODO")
    assert result == "This task contains a #TODO." 

def test_string_does_not_contain_to_do():
    result = to_do("Task2 have already walked dog.")
    assert result == "This task does not contain a #TODO." 

def test_if_argument_is_string():
    with pytest.raises(Exception) as e:
        to_do(7)
    error_message = str(e.value)
    assert error_message == "Argument must be a string"

        