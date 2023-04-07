class Parser:

    def __init__(self, lexemes):
        self.lexemes = lexemes
        self.position = -1
        self.length = len(lexemes)


    def parser(self):
        self.next()

    def next(self):
        if self.position < self.length:
            self.position += 1
        else:
            raise Exception("Список лексем закончился")

