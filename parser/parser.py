from .ast import NumberNode, ASTNode, BinOpNode, UnaryOpNode
from .token import Token, TokenType


class Parser:
    def __init__(self, tokens: list[Token]):
        self._tokens = tokens
        self._pos = 0
        self._current_token = self._tokens[self._pos]

    def _eat(self, token_type: TokenType):
        if self._current_token.t_type == token_type:
            self._pos += 1
            self._current_token = self._tokens[self._pos]
        else:
            raise Exception(f'Syntax Error: Expected: {token_type}, Got: {self._current_token.t_type}')

    def _factor(self) -> ASTNode:
        token = self._current_token
        if token.t_type == TokenType.NUMBER:
            self._eat(TokenType.NUMBER)
            return NumberNode(token)
        elif token.t_type == TokenType.L_PAREN:
            self._eat(TokenType.L_PAREN)
            node: ASTNode = self._expression()
            self._eat(TokenType.R_PAREN)
            return node

    def _unary(self) -> ASTNode:
        token = self._current_token

        if token.t_type in (TokenType.PLUS, TokenType.MINUS):
            self._eat(token.t_type)
            return UnaryOpNode(op_token=token, expr=self._unary())

        return self._factor()

    def _term(self) -> ASTNode:
        node: ASTNode = self._unary()

        while self._current_token.t_type in (TokenType.STAR, TokenType.SLASH):
            op: Token = self._current_token
            self._eat(op.t_type)

            # Create a tree branch: left is the previous node, right is the next factor
            node: ASTNode = BinOpNode(left=node, op_token=op, right=self._unary())

        return node

    def _expression(self) -> ASTNode:
        node: ASTNode = self._term()

        while self._current_token.t_type in (TokenType.PLUS, TokenType.MINUS):
            op: Token = self._current_token
            self._eat(op.t_type)

            # Create a tree branch: left is the previous node, right is the next term
            node: ASTNode = BinOpNode(left=node, op_token=op, right=self._term())

        return node

    def parse(self):
        return self._expression()
