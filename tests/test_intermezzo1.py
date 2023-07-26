from lib.intermezzo1 import * 

def test_intermezzo1_hello_kay():
    result = say_hello("kay")
    assert result == "hello kay"