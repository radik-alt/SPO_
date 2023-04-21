class Node:

    def __init__(self, value, type=None, children=None):
        self.value = value
        self.type = type
        self.children = children or []

    def __str__(self):
        return f"value: {self.value}, type:{self.type}"

    def check_types(self):
        if not isinstance(self.value, (int, float)):
            raise Exception("Не соотвествует типу данных int или float")

    def check_logic(self):
        if self.type != "Integer":
            raise Exception("Не правильная логика! Можно присваивать только Integer")


class ArithmeticNode(Node):
    def __init__(self, value, children=None):
        super().__init__(value, "Arithmetic", children)

    def check_types(self):
        if self.children is None:
            raise Exception("Ошибка при создании узла")

        for child in self.children:
            if not isinstance(child.value, (int, float)):
                raise TypeError(f"Expected int or float, got {type(child.value)} for child {child}")


class LogicNode(Node):

    def __init__(self, value, children=None):
        super().__init__(value, "Logic", children)

    def check_types(self):
        if self.children is None:
            raise Exception("Ошибка при создании узла")

        for child in self.children:
            if not isinstance(child.value, (int, float)):
                raise TypeError(f"Expected int or float, got {type(child.value)} for child {child}")


class Parser:

    def __init__(self, lexemes):
        self.lexemes = lexemes
        self.position = -1
        self.length = len(lexemes) - 1

    def parse(self):
        node_list = []
        while self.position < self.length:
            node_list.append(self.next_node())
        return node_list

    def next_node(self):
        self.position += 1
        value = self.lexemes[self.position].value
        type = self.lexemes[self.position].type
        children = []
        node = Node(value, type, children)
        if value == "for":
            node.children.append(self.for_range())
        elif type == "Identifier":
            next_value = self.lexemes[self.position + 1].value if self.position < self.length else ""
            if next_value == "=":
                node.children.append(self.assignment())
        elif value in ["+", "-", "*", "/"]:
            node.children.append(ArithmeticNode(value))
            node.children.append(self.next_node())
            node.children.append(self.next_node())
            node.children[0].check_types()
        return node

    def assignment(self):
        children = []
        if self.lexemes[self.position].type == "Identifier":
            children.append(Node(self.lexemes[self.position].value, "Identifier"))
            self.position += 1
            if self.lexemes[self.position].value == "=" and self.lexemes[self.position].type == "Assignment":
                children.append(Node("=", "Assignment"))
                self.position += 1
                nex_node = Node(self.lexemes[self.position].value, self.lexemes[self.position].type)
                nex_node.check_logic()
                if self.lexemes[self.position].type == "Integer":
                    nex_node.value = int(nex_node.value)
                    nex_node.check_types()
                    children.append(nex_node)
                return Node("assignment", "Expression", children)
            else:
                raise Exception("Ошибка в присваивании")
        else:
            raise Exception("Ошибка в идентификаторе в присваивании")

    def for_range(self):
        children = []
        if self.lexemes[self.position].value == "for" and self.lexemes[self.position].type == "Keyword":
            children.append(Node("for", "Keyword"))
            self.position += 1
            if self.lexemes[self.position].type == "Identifier":
                children.append(Node(self.lexemes[self.position].value, "Identifier"))
                self.position += 1
                if self.lexemes[self.position].value == "in" and self.lexemes[self.position].type == "Keyword":
                    children.append(Node("in", "Keyword"))
                    self.position += 1
                    if self.lexemes[self.position].value == "range" and self.lexemes[
                        self.position].type == "Identifier":
                        children.append(Node("range", "Identifier"))
                        self.position += 1
                        if self.lexemes[self.position].value == "(" and self.lexemes[
                            self.position].type == "LeftParenthesis":
                            children.append(Node("(", "LeftParenthesis"))
                            self.position += 1
                            if self.lexemes[self.position].type == "Identifier":
                                children.append(Node(self.lexemes[self.position].value, "Identifier"))
                                self.position += 1
                                if self.lexemes[self.position].value == ")" and self.lexemes[
                                    self.position].type == "RightParenthesis":
                                    children.append(Node(")", "RightParenthesis"))
                                    self.position += 1
                                    if self.lexemes[self.position].value == ":" and self.lexemes[
                                        self.position].type == "Colon":
                                        children.append(Node(":", "Colon"))
                                        self.position += 1
                                        return Node("for_range", "Expression", children)
                                    else:
                                        raise Exception("Ошибка : после range")
                                else:
                                    raise Exception("Ошибка ) после идентификатора")
                            else:
                                raise Exception("Ошибка идентификатора в range")
                        else:
                            raise Exception("Ошибка ( после range")
                    else:
                        raise Exception("Ошибка range после in")
                else:
                    raise Exception("Ошибка in после идентификатора")
            else:
                raise Exception("Ошибка идентификатора в for")
        else:
            raise Exception("Ошибка for, посмотрите как написали for")
