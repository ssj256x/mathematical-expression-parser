from .ast import NumberNode, BinOpNode


def print_ast(node, prefix="", is_last=True):
    if node is None:
        return

    # Determine the pointer symbol for the current node
    marker = "└── " if is_last else "├── "
    # marker = "+-- " if is_last else "|-- "

    # Format the node description (Subtype + Value)
    if isinstance(node, NumberNode):
        print(f"{prefix}{marker}({node.value})")
    elif isinstance(node, BinOpNode):
        print(f"{prefix}{marker}{node.op_token.value}")

        # Prepare the prefix for the children
        # If this node is the last child, its descendants shouldn't have a vertical line anchoring back to it
        new_prefix = prefix + ("    " if is_last else "│   ")
        # new_prefix = prefix + ("    " if is_last else "|   ")

        # A Binary Operator node always has exactly two children: Left and Right.
        # Right is processed last, so is_last=False for Left, and is_last=True for Right.
        print_ast(node.left, new_prefix, is_last=False)
        print_ast(node.right, new_prefix, is_last=True)
