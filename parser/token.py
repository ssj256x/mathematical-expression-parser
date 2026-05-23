from enum import Enum


class TokenType(Enum):
    PLUS = '+'
    MINUS = '-'
    STAR = '*'
    SLASH = '/'
    L_PAREN = '('
    R_PAREN = ')'
    NUMBER = 'NUMBER'
    EOF = '\0'


class Token:
    def __init__(self, t_type: TokenType, value: str):
        self.t_type = t_type
        self.value = value

    def __repr__(self):
        return f"Token({self.t_type.name}, '{self.value}')"
