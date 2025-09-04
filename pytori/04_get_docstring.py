import ast

# docstringを持つ関数を含むPythonコードの文字列
source_code = """
def my_function():
    '''This is the docstring for my_function.

    It explains what the function does.
    '''
    return "Hello, World!"

class MyClass:
    "This is the docstring for MyClass."
    def __init__(self):
        pass
"""

module_docstring = ast.get_docstring(ast.parse(source_code))
print(f"Module Docstring: {module_docstring}")