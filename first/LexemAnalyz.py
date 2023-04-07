import re

from first.Token import Token


# Функция разбора кода на лексемы
def lex_parse(code):
    # Список лексем
    lexemes = []

    # Регулярное выражение для лексического анализа
    token_pattern = r'(\bfor\b|\bin\b|[a-zA-Z_][a-zA-Z0-9_]*|[0-9]+|[+=:()])'

    # Поиск всех лексем в коде
    tokens = re.findall(token_pattern, code)

    # Маппинг регулярных выражений на типы лексем
    lexeme_types = {
        'for': 'Keyword',
        'in': 'Keyword',
        '+': 'Addition',
        '=': 'Assignment',
        ':': 'Colon',
        '(': 'LeftParenthesis',
        ')': 'RightParenthesis',
    }

    # Обход всех найденных лексем и добавление их в список лексем
    for token in tokens:
        # Определение типа лексемы
        lex_type = lexeme_types.get(token, 'Identifier' if token.isalpha() else 'Integer')
        lexeme = Token(lex_type, token)
        lexemes.append(lexeme)

    return lexemes




# Тестовый код
