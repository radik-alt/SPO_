from first import LexemAnalyz
from four.GeneratorJsCode import GeneratorJsCode
from second.Parser import Parser

code = """
counter = 5
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
            level += 2
            print_tree(child, level)
    else:
        level = 0




def main():
    lexemes = LexemAnalyz.lex_parse(code)
    print_lexemes(lexemes)

    print("\n")

    parser = Parser(lexemes)
    tree = parser.parse()
    print_node_list(tree)

    # js_code = generate_js_code(tree)
    # print(js_code)


if __name__ == '__main__':
    main()
