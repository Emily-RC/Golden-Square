1. Describe the problem

User needs a class that will check grammar. Firstly to check if the text starts with a capital letter and ends in appropiate punctuation. 
There should also be a function that checks the percentage of the texts checked so far that passed the check defined in the above method. 

2. Design the function signature.
    The signature of a class includes:
    2 different functions:
        1. def check():
            Parameters: text
            Returns: a boolean True if text starts with capital letter and ends in approp. punctuation 
        2. def percentage_good():
            Parameters: none
            Returns: the percentage of texts checked so far that passed the check
            defined in the `check` method. The number 55 represents 55%.

3. Examples as Tests
   
    Given the text begins with a capital letter and ends in the right punctuation
    Returns True 

    grammar_stats = GrammarStats("Hello my name is Emily.")
    grammar_stats.check("Hello my name is Emily.") ==> True 


    Given the number of texts that have passed the check defined in the check method
    Returns an integer that represents the percentage
    
    grammar_stats = GrammarStats("Hello my name is Emily.")
    grammar_stats = GrammarStats("hello my name is Emily")
    grammar_stats.percentage_good() ==> 50

 
