from lib.count_words import * 

def test_count_words():
    input_str1 = "Hello my name is Emily and I am from London"
    output1 = 10 
    assert count_words(input_str1) == output1



# def count_words(str1):
#     words = str1.split()
#     return len(words)