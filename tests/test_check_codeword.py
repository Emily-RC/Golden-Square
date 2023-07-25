from lib.check_codeword import *

def test_check_codeword():
    assert check_codeword("Bubble") == "WRONG!"
    assert check_codeword("hole") == "Close, but nope."
    assert check_codeword("horse") == "Correct! Come in."

        
# def check_codeword(codeword):
#     if codeword == "horse":
#         return "Correct! Come in."
#     elif codeword[0] == "h" and codeword[-1] == "e":
#         return "Close, but nope."
#     else: return "WRONG!"