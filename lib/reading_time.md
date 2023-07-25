1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

<!-- As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.  -->

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def estimate_reading_time(words_count):
    extracts reading time from words in a given text
    assumes reading time is 200 words a minute 
        calculate reading time by words_count / 200 

Parameters - words_in_text
    Pass through an int which is number of words in given text 

return value - will be the reading time 
    f string "The reading time for this text is estimated to be {x} minutes" 

Side effects - We are not expecting any side effects


3. Create Examples as Tests
Make a list of examples of what the function will take and return.

input is an integer which represents the words_count in given text 
output string: "The reading time for this text is estimated to be {x} minutes" 

Given a text with 300 words 
It returns a string that says "The reading time for this text is estimated to be 1.5 minutes" 

Given a text with 120,000 words 
It returns a string that says "The reading time for this text is estimated to be 600 minutes" 


4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
Ensure all test function names are unique, otherwise pytest will ignore them!