from cmath import inf
from tracemalloc import stop
from turtle import pos, st
from ds import Stack


def infix_to_postfix(infix):
    stack = Stack()
    postfix= ""
    high_operands = ["*", "/"]
    low_operands = ["+", "-"]

    for c in infix:
        if c.isalnum():
            postfix += c

        elif c == "(":
            stack.push(c)

        elif c == ")":
            postfix += stack.pop()

        elif c in high_operands:
            while stack.top in high_operands:
                postfix += stack.pop()

            stack.push(c)

        elif c in low_operands:
            while stack.top in high_operands or stack.top in low_operands:
                postfix += stack.pop() 

            stack.push(c)

        print(c, " ", postfix)

    while not stack.is_empty:
        c = stack.pop()
        if c != "(":
            postfix += stack.pop()

    return postfix


def main():
    infix = "(A+B/C*(D+E)-F)"
    print(infix_to_postfix(infix))


if __name__ == "__main__":
    main()