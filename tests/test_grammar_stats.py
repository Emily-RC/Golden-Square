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

# def test_percentage_good_zero_texts(self):
#     grammar_stats = GrammarStats()
#     self.assertEqual(grammar_stats.percentage_good(), 0)

# def test_percentage_good_some_passed(self):
#     grammar_stats = GrammarStats()
#     grammar_stats.total_texts = 10
#     grammar_stats.passed_texts = 7
#     self.assertEqual(grammar_stats.percentage_good(), 70)

# def test_percentage_good_all_passed(self):
#     grammar_stats = GrammarStats()
#     grammar_stats.total_texts = 5
#     grammar_stats.passed_texts = 5
#     self.assertEqual(grammar_stats.percentage_good(), 100)

# def test_percentage_good_no_texts(self):
#     grammar_stats = GrammarStats()
#     self.assertEqual(grammar_stats.percentage_good(), 0)