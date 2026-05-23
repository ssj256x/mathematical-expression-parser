from parser import Lexer, Parser, print_ast, Interpreter

# expr = '((1 + 2) * 3) + 4'
expr = '-((1 + 2) * 3) + 4'

lexer = Lexer(expr)
tokens = lexer.lex()

parser = Parser(tokens)
root = parser.parse()

print_ast(node=root)
interpreter = Interpreter()

print(f'Ans: {interpreter.evaluate(root)}')