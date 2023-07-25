import pytest
from lib.reading_time import *

def test_check_output_is_accurate():
    result = estimate_reading_time(300)
    assert result == 1.5 

def test_check_argument_is_integer():
    with pytest.raises(Exception) as e:
        estimate_reading_time("300")
    error_message = str(e.value)
    assert error_message == "Argument must be an integer."
        
