from .token import Token


class ASTNode:
    pass


class NumberNode(ASTNode):
    def __init__(self, token: Token):
        try:
            self.value = int(token.value)
        except ValueError:
            self.value = float(token.value)


class BinOpNode(ASTNode):
    def __init__(self, left: ASTNode, op_token: Token, right: ASTNode):
        self.left = left
        self.op_token = op_token.t_type
        self.right = right


class UnaryOpNode(ASTNode):
    def __init__(self, op_token: Token, expr: ASTNode):
        self.op_token = op_token.t_type
        self.expr = expr