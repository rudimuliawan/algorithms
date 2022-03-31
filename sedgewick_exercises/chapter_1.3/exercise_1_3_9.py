from ast import operator
from ds import Stack


def balancing_expression(expression):
    operators = Stack()    
    operands = Stack()

    for c in expression:
        if c.isdigit():
            operands.push(c)

        elif c in ["+", "-", ":", "*"]:
            operators.push(c)

        elif c == ")":
            operand_a = operands.pop()
            operand_b = operands.pop()
            operator = operators.pop()

            sub_expression = f"({operand_b} {operator} {operand_a})"
            operands.push(sub_expression)

    return operands.pop()


def main():
    expression = "1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )"
    print(balancing_expression(expression))

if __name__ == "__main__":
    main()
