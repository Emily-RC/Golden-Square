from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("family")
    gratitudes.add("friends")
    result = gratitudes.format()
    assert result == f"Be grateful for: family, friends"


#class Gratitudes:
#     def __init__(self):
#         self.gratitudes = []

#     def add(self, gratitude):
#         self.gratitudes.append(gratitude)

#     def format(self):
#         formatted = "Be grateful for: "
#         formatted += ", ".join(self.gratitudes)
#         return formatted


