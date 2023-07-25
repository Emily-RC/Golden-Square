1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.


2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def grammar_checker(string):

    check the sentence begins with a capital letter
    check the sentence ends with suitable punctuation 

suitable punctuation will be defined as !?.

    Parameter:
        string = this will be the given text inputted 
    
    Returns:
        a True or False value based on whether the string meets the two conditions

    Side effects:
        This function doesn't print anything or have any other side-effects 



3. Create Examples as Tests
Make a list of examples of what the function will take and return.


    Given a sentence that starts with a capital and ends with suitable punctuation
    It returns True 

    Given a sentence that doesn't start with a capital letter but does have suitable punctions
    It returns False 

    Given a sentence that does start with a capital letter but doesn't have suitable punctions
    It returns False 

    Given a sentence that doesn't start with a capital letter and doesn't have suitable punctions
    It returns False 


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