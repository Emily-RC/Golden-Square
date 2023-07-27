class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.passed_texts = 0

    def check(self, text):
        if text[0].isupper() and text[-1] in "!.?":
            return True
        else: 
            return False
        
    def percentage_good(self):
        if self.total_texts == 0:
            return 0

        return (self.passed_texts / self.total_texts) * 100

grammar_stats = GrammarStats()
result = grammar_stats.check("Hello my name is Emily.")
print(result)


    # def test_grammar_stats_check():
    # grammar_stats = GrammarStats("Hello my name is Emily.")
    # result = grammar_stats.check()
    # assert result == True


    # def format(self):
    #     return f"{self.title}: {self.contents}"

    # def count_words(self):
    #     word = self.contents.split()
    #     return len(word)

    # def reading_time(self, wpm):
    #     words = self.contents.split()
    #     word_count = len(words)
    #     return word_count / 200
    
    # def reading_chunk(self, wpm, minutes):
    #     chunk_of_words = int(wpm * minutes)
    #     text = " ".join(["word" for i in range(1, chunk_of_words +1)])
    #     return text


