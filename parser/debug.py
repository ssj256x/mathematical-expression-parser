from .ast import NumberNode, BinOpNode, UnaryOpNode


def print_ast(node, prefix="", is_last=True):
    if node is None:
        return

    # Determine the pointer symbol for the current node
    marker = "└── " if is_last else "├── "

    # Format the node description (Subtype + Value)
    match node:
        case NumberNode():
            print(f"{prefix}{marker}({node.value})")

        case BinOpNode():
            print(f"{prefix}{marker}{node.op_token.value}")

            # Prepare the prefix for the children
            new_prefix = prefix + ("    " if is_last else "│   ")

            # A Binary Operator node always has exactly two children: Left and Right.
            print_ast(node.left, new_prefix, is_last=False)
            print_ast(node.right, new_prefix, is_last=True)

        case UnaryOpNode():
            print(f"{prefix}{marker}{node.op_token.value}")
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_ast(node.expr, new_prefix, is_last=True)

        case _:  # Default case for any other node type
            print(f"{prefix}{marker}Unknown Node Type: {type(node)}")
