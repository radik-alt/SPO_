class Lex:
    def __init__(self, lex_type, value):
        self.lex_type = lex_type
        self.value = value

    def __str__(self):
        return f'Type: {self.lex_type}, Value: {self.value}'