from .token import Token, TokenType


class Lexer:
    def __init__(self, text):
        self._text = text
        self._pos = 0
        self._current_char = text[0] if text else None

    def _advance(self):
        self._pos += 1
        if self._pos < len(self._text):
            self._current_char = self._text[self._pos]
        else:
            self._current_char = None

    def _peek(self):
        peek_pos = self._pos + 1
        if peek_pos < len(self._text):
            return self._text[peek_pos]
        return None

    def _get_number(self):
        num = ''

        while self._current_char is not None and (self._current_char.isdigit() or self._current_char == '.'):
            if self._current_char == '.':
                if '.' in num:
                    raise Exception(f'Pos: {self._pos} Number cannot have two decimal dots')

                if not (self._peek() and self._peek().isdigit()) and not num:
                    # This handles the case where we start with a dot but no digits follow
                    break

            num += self._current_char
            self._advance()

        if num == '.':
            raise Exception(f"Pos: {self._pos} Invalid number '.'")

        if num and num[0] == '.':
            num = '0' + num

        return num

    def _get_next_token(self):
        while self._current_char is not None:
            match self._current_char:
                case c if c.isspace():
                    self._advance()
                    continue

                case '+':
                    self._advance()
                    return Token(TokenType.PLUS, '+')

                case '-':
                    self._advance()
                    return Token(TokenType.MINUS, '-')

                case '*':
                    self._advance()
                    return Token(TokenType.STAR, '*')

                case '/':
                    self._advance()
                    return Token(TokenType.SLASH, '/')

                case '(':
                    self._advance()
                    return Token(TokenType.L_PAREN, '(')

                case ')':
                    self._advance()
                    return Token(TokenType.R_PAREN, ')')

                case c if c.isdigit() or c == '.':
                    return Token(TokenType.NUMBER, self._get_number())

                case _:
                    raise Exception(f'Pos: {self._pos}, Parse Error, Invalid character : {self._current_char}')

        return Token(TokenType.EOF, '\0')

    def lex(self) -> list[Token]:
        tokens = []

        while True:
            cur_token = self._get_next_token()
            tokens.append(cur_token)

            if cur_token.t_type == TokenType.EOF:
                break

        return tokens
