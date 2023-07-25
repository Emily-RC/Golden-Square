from lib.grammar_checker import * 

def test_grammar_checker_both_true():
    input1 = "This sentence passes the test."
    assert grammar_checker(input1) == True

def test_grammar_check_if_capital_lower_only():
    input2 = "this sentence does not pass the test."
    assert grammar_checker(input2) == False

def test_grammar_check_if_unsuitable_punctuation():
    input3 = "This sentence does not pass the test"
    assert grammar_checker(input3) == False

def test_grammar_check_if_neither_conditions_met():
    input4 = "this sentence does not pass the test"
    assert grammar_checker(input4) == False