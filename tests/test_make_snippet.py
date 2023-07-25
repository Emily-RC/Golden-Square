from lib.make_snippet import *

def test_make_snippet():
    input_str1 = "Hello my name is Emily and I am from London"
    output1 = "Hello my name is Emily ..."
    assert make_snippet(input_str1) == output1

    input_str2 = "Testing testing one two three"
    output2 = "Testing testing one two three"
    assert make_snippet(input_str2) == output2

    input_str3 = ""
    output3 = ""
    assert make_snippet(input_str3) == output3




# def make_snippet(str1):
#     words = str1.split()
#     snippet = " ".join(words[0:5])
#     if len(words) > 5:
#         snippet += " ..."
#     return snippet

# snippet = make_snippet("hello my name is Emily and I am from London")
# print(snippet)
