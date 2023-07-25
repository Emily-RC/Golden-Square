from lib.report_length import * 

def test_report_length():
    assert report_length("Hello world") == "This string was 11 characters long."
    assert report_length("My name is Emily") == "This string was 16 characters long."



# def report_length(str):
#     length = len(str)
#     return f"This string was {length} characters long.