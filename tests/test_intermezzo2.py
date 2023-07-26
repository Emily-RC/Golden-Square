from lib.intermezzo2 import * 

def test_check_output():
    result = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert result == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"