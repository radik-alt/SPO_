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
        print_node(node)

def print_node(node, level=0):
    indent = "  " * level
    print(f"{indent}Value: {node.value}, Type: {node.type}")
    if node.children:
        print(f"{indent}Children:")
        for child in node.children:
            print_node(child, level=level+1)

def main():
    lexemes = LexemAnalyz.lex_parse(code)
    # print_lexemes(lexemes)

    parser = Parser(lexemes)
    print_node_list(parser.parse())


if __name__ == '__main__':
    main()
