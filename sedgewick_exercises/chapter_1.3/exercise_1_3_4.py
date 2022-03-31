from ds import Stack
from unittest import TestCase


def is_parentheses_balance(input):
    stack = Stack()

    for c in input:
        if c in ["[", "(", "{"]:
            stack.push(c)
            continue
        
        # check right parentheses
        try:
            rp = stack.pop()
        except:
            return False
        
        if c == "]" and rp == "[":
            continue

        elif c == "}" and rp == "{":
            continue

        elif c == ")" and rp == "(":
            continue

        else:
            return False

    return True


def main():
    print(is_parentheses_balance("[()]{}{[()()]()}"))
    print(is_parentheses_balance("[({({})})]"))
    print(is_parentheses_balance("[(][)]"))
    print(is_parentheses_balance("[([)]"))
    

if __name__ == "__main__":
    main()
