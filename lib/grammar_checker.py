
def grammar_checker(string):
    if string[0].isupper() and string[-1] in "!.?":
        return True 
    else:
        return False