# Arithmetic Expression Parser

This project implements a simple arithmetic expression parser in Python. It takes a mathematical expression as a string,
tokenizes it, builds an Abstract Syntax Tree (AST), and then interprets the AST to evaluate the expression.

## Features

* **Lexical Analysis (Lexer)**: Converts the input string into a stream of tokens.
* **Syntactic Analysis (Parser)**: Builds an Abstract Syntax Tree (AST) from the token stream based on a defined
  grammar.
* **Abstract Syntax Tree (AST)**: Represents the hierarchical structure of the expression.
* **Interpreter**: Traverses the AST to evaluate the expression and compute the result.
* **Supports**:
    * Basic arithmetic operations: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`).
    * Unary plus and minus (`+`, `-`).
    * Parentheses for grouping expressions.
    * Integer and floating-point numbers.
* **AST Visualization**: Includes a utility to print a visual representation of the generated AST.

## Getting Started

### Prerequisites

* Python 3.10 or higher (due to the use of `match/case` statements).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ssj256x/mathematical-expression-parser
   cd arithmetic-expression-parser
   ```

2. **Install dependencies (using `uv` or `pip`):**
   If you have `uv` installed:
   ```bash
   uv sync
   ```
   Or using `pip`:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt # You might need to create a requirements.txt if not present
   ```
   *Note: This project currently has no external dependencies beyond standard Python libraries, so `uv sync`
   or `pip install` might not be strictly necessary if you don't have a `pyproject.toml` or `requirements.txt` with
   external packages.*

## Usage

To run the example expression defined in `main.py`:

```bash
python main.py
```

The `main.py` file currently evaluates the expression `-((1 + 2) * 3) + 4`.

You can modify the `expr` variable in `main.py` to test different expressions:

```python
# main.py
# ...
expr = '10 * (2 + 3) / 5 - -1'  # Example of a different expression
# ...
```

### Example Output

For `expr = '-((1 + 2) * 3) + 4'`, the output will look something like this:

```
└── -
    ├── *
    │   ├── (3)
    │   └── (3)
    └── (4)
Ans: -5.0
```

*(Note: The AST representation might vary slightly based on the exact implementation of `print_ast` and the order of
operations, but the final answer should be consistent.)*

## Project Structure

The core logic of the parser is organized within the `parser/` directory:

```
arithmetic-expression-parser/
├── main.py
├── pyproject.toml
├── uv.lock
└── parser/
    ├── __init__.py
    ├── ast.py
    ├── debug.py
    ├── grammar.bnf
    ├── interpreter.py
    ├── lexer.py
    ├── parser.py
    └── token.py
```

* **`main.py`**: The entry point of the application. It initializes the Lexer, Parser, and Interpreter, then prints the
  AST and the final result.
* **`parser/ast.py`**: Defines the Abstract Syntax Tree (AST) nodes, such as `NumberNode`, `BinOpNode` (binary
  operations), and `UnaryOpNode` (unary operations).
* **`parser/debug.py`**: Contains the `print_ast` function, a utility for visualizing the generated AST in a tree-like
  structure.
* **`parser/grammar.bnf`**: Specifies the grammar of the arithmetic expressions in Backus-Naur Form (BNF).
* **`parser/interpreter.py`**: Implements the `Interpreter` class, which traverses the AST and evaluates the expression
  to produce a numerical result.
* **`parser/lexer.py`**: Contains the `Lexer` class, responsible for converting the input string into a sequence of
  `Token` objects.
* **`parser/parser.py`**: Implements the `Parser` class, which takes the token stream from the lexer and constructs the
  AST.
* **`parser/token.py`**: Defines the `Token` class and `TokenType` enum, representing the basic building blocks of the
  language.

## Grammar (BNF)

The grammar for the arithmetic expressions is defined as follows:

```bnf
expression ::= term (('+' | '-') term)*
term       ::= unary (('*' | '/') unary)*
unary      ::= ('+' | '-') unary | factor
factor     ::= NUMBER | '(' expression ')'
NUMBER     ::= digit+ ('.' digit+)?
digit      ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
```
