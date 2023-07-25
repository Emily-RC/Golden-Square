from lib.string_builder import * 

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("Hello world")
    string_builder.size(11)
    result = string_builder.output()
    assert result == "Hello world"


# class StringBuilder:
#     def __init__(self):
#         self.str = ""

#     def add(self, str):
#         self.str += str

#     def size(self):
#         return len(self.str)

#     def output(self):
#         return self.str