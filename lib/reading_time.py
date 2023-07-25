def estimate_reading_time(word_count):
    if type(word_count) != int:
        raise Exception("Argument must be an integer.")
    else: 
        return word_count / 200


# def test_check_argument_is_integer():
#     with pytest.raises(Exception) as e:
#         estimate_reading_time("300")
#     error_message = str(e.value)
#     assert error_message == "Argument must be an integer."
        
# class PasswordChecker:
#     def check(self, password):
#         if len(password) >= 8:
#             return True
#         else:
#             raise Exception("Invalid password, must be 8+ characters.")