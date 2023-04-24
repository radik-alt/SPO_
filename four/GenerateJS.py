class GenerateJS:

    def __init__(self, tree):
        self.tree = tree
        self.code = ""

    def start(self):
        for item in self.tree:
            self.js_code(item)

        print(self.code)

    def js_code(self, tree):
        children = tree.children
        if children is not None:
            for item in children:
                if item.value == "assignment" and item.type == "Expression":
                    self.code += f"let {item.children[0].value} = {item.children[2].value};\n"
                elif item.value == "for_range" and item.type == "Expression":
                    self.code += f"{item.children[0].value} ( {item.children[1].value} = 0; {item.children[1].value} < {item.children[5].value}; {item.children[1].value}++ )"
                    self.code += "{\n"
                elif item.type == "Arithmetic":
                    self.code += f"\tcounter {item.value}= "
                elif item.type == "Integer":
                    self.code += f"{item.value};\n"
                    self.code += f"\tconsole.log(n);\n"
                    self.code += "}"

    def save_file(self):
        with open("example.js", "w") as file:
            file.write(self.code)
