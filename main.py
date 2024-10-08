from first import LexemAnalyz
from four.GenerateJS import GenerateJS
from second.Parser import Parser

code = """
counter = 5
n = 12

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
    print("Список лексем: ")
    lexemes = LexemAnalyz.lex_parse(code)
    print_lexemes(lexemes)

    print("\n")

    print("AST дерево: ")
    parser = Parser(lexemes)
    tree = parser.parse()
    print_node_list(tree)

    print("\n")

    js_code = GenerateJS(tree)
    print("Код на JS:\n")
    js_code.start()
    js_code.save_file()

if __name__ == '__main__':
    main()
