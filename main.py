from first import LexemAnalyz
from second.Parser import Parser

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


def print_node_list(node_list):
    for node in node_list:
        print_tree(node)


def print_tree(node, level=0):
    if node is None:
        return
    print(" " * level + str(node))
    if node.children is not None:
        for child in node.children:
            print_tree(child, level=level+2)

def main():
    lexemes = LexemAnalyz.lex_parse(code)
    print_lexemes(lexemes)

    parser = Parser(lexemes)
    print_node_list(parser.parse())


if __name__ == '__main__':
    main()
