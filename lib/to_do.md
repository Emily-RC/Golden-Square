{{PROBLEM}} Function Design Recipe
Copy this into a recipe.md in your project and fill it out.

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.


2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

Function - 
def check_for_to_do(texts): 
function definition is to check a string called "texts" for the string #TODO
Function will include an if/else statement that sets a variable to True or False based on whether condition is met 

Parameters - 
takes "texts" as an argument 
"texts" is the input and the data type is a string

Return value - 
String that indicates whether the texts string contains #TODO 


Side effects - 
This function doesn't print anything or have any other side-effects


3. Create Examples as Tests
Make a list of examples of what the function will take and return.

Given a string that contains #TODO
It returns "This task contains a #TODO." 

Given a string that does not contain #TODO
It returns "This task does not contain a #TODO." 


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