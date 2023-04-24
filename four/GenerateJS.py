class GenerateJS:

    def __init__(self, tree):
        self.tree = tree
        self.code = ""

    def start(self):
        for item in self.tree:
            self.js_code(item)

    def js_code(self, tree):
        children = tree.children
        if children is not None:
            for item in children:
                if item.value == "assignment" and item.type == "Expression":
                    self.code += f"let {item.children[0].value} = {item.children[2].value};"
                elif item.value == "for_range" and item.type == "Expression":
                    self.code += f"{item.children[0].value} ( {item.children[1].value} = 0; {item.children[1].value} < {item.children[5].value}; {item.children[1].value}++ )"
                    self.code += "{\n"
                else:
                    self.code += f"{item.value}",
                    self.code += "}"
