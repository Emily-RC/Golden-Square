import pytest
from lib.password_checker import *

def test_password_checker():
    password_checker = PasswordChecker()
    password_checker.check("12345678!")
    assert password_checker.check("12345678!") == True

def test_passsword_checker1():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("1234")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

# class PasswordChecker:
#     def check(self, password):
#         if len(password) >= 8:
#             return True
#         else:
#             raise Exception("Invalid password, must be 8+ characters.")