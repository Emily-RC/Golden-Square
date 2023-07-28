from lib.grammar_stats import *

def test_grammar_stats_check():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello my name is Emily.")
    assert result == True 


def test_percentage_of_passed_checke():
    grammar_stats = GrammarStats() 
    result = grammar_stats.check("Hello my name is Emily.") 
    result = grammar_stats.check("Hello my name is Emily.") 
    result = grammar_stats.check("Hello my name is Emily.") 
    result = grammar_stats.check("Hello my name is Emily.") 
    assert result 
