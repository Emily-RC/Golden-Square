1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

class Diary():

initialise the class with two classes, text and todo

Create a function to return a list of tasks from a to do list - function to format 
Parameters will be text 
Return will be list of tasks 

Create a function that remove tasks once completed 
Parameters will be tasks 
Return new list with completed tasks removed (.append)


3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

Given a text
Return in formatted list structure - return list 

diary = Diary("Walk the dog")
result = diary.format("Task: Walk the dog")


Given a list of tasks some of which are completed 
If completed remove and returns a new list without completed tasks 

diary = Diary("Walk the dog")
diary.format("Task: Walk the dog")
diary.sort => removes completed
result = diary.append("Task: Walk the dog") => completed removed 


4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.