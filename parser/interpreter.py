from . import TokenType
from .ast import ASTNode, NumberNode, BinOpNode, UnaryOpNode


class Interpreter:
    def evaluate(self, node: ASTNode):

        if isinstance(node, NumberNode):
            return node.value

        if isinstance(node, UnaryOpNode):
            value = self.evaluate(node.expr)

            match node.op_token:
                case TokenType.MINUS:
                    return -value
                case TokenType.PLUS:
                    return +value
                case c:
                    raise Exception(f'Unexpected Token : {c}')

        if isinstance(node, BinOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            match node.op_token:
                case TokenType.PLUS:
                    return left + right
                case TokenType.MINUS:
                    return left - right
                case TokenType.STAR:
                    return left * right
                case TokenType.SLASH:
                    if right == 0:
                        raise Exception('Runtime Error: / by 0')
                    return left / right
                case c:
                    raise Exception(f'Unexpected Token : {c}')

        raise Exception(f'Unknown Node Type : {type(node)}')
