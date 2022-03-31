from ds import Stack


def main():
    stack = Stack()

    stack.push(2)
    print(stack.top)

    stack.push(3)
    print(stack.top)


if __name__ == "__main__":
    main()