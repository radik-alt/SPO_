from first import LexemAnalyz

code = """
counter = 0
n = 5

for i in range ( n ):
    counter += 1
"""


# Функция вывода лексем
def print_lexemes(lexemes):
    for lexeme in lexemes:
        print(f'Type: {lexeme.type}, Value: {lexeme.value}')


def main():
    lexemes = LexemAnalyz.lex_parse(code)
    print_lexemes(lexemes)


if __name__ == '__main__':
    main()

