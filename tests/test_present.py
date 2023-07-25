import pytest
from lib.present import *

def test_present():
    present = Present()
    present.wrap("bike")
    assert present.unwrap() == "bike"
    
def test_present1():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_present2():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap("book")
        present.wrap("bike")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
    
    
    # present.wrap("book")
    # unwrapped_content = present.unwrap()
    # assert unwrapped_content == "book" 


    # class Present:
    # def __init__(self):
    #     self.contents = None

    # def wrap(self, contents):
    #     if self.contents is not None:
    #         raise Exception("A contents has already been wrapped.")
    #     self.contents = contents

    # def unwrap(self):
    #     if self.contents is None:
    #         raise Exception("No contents have been wrapped.")
    #     return self.contents