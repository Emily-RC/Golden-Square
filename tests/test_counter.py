from lib.counter import * 

def test_counter():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

# class Counter:
#     def __init__(self):
#         self.count = 0

#     def add(self, num):
#         self.count += num

#     def report(self):
#         return f"Counted to {self.count} so far."
