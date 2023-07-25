def make_snippet(str1):
    words = str1.split()
    snippet = " ".join(words[0:5])
    if len(words) > 5:
        snippet += " ..."
    return snippet

# snippet = make_snippet("hello my name is Emily and I am from London")
# print(snippet)

