"""Basic Math interpreter for the user"""
# pylint: disable=eval-used


def external_prompt_math():
    """Used to do quick math calculations"""
    print("syntax: num operator num")
    print(
        "+ is Addition, - is subtraction, * is Multiplication / is division and q to quit"
    )

    while True:
        user_input = input("Enter Question> ")

        if user_input.lower in ["q", "quit", "escape"]:
            break

        try:
            print(eval(user_input))

        except ValueError as exception:
            print("Error")
            print()
            print(exception)
            print()


def add(num1: int, num2: int):
    """Can add two numbers

    Args:
        num1 (int): no. 1
        num2 (int): no. 2
    """
    return num1 + num2


def subtract(num1: int, num2: int):
    """Can subtract two numbers

    Args:
        num1 (int): no. 1
        num2 (int): no. 2
    """
    return num1 - num2


def multiply(num1: int, num2: int):
    """Can multiply two numbers

    Args:
        num1 (int): no. 1
        num2 (int): no. 2
    """
    return num1 * num2


def divide(num1: int, num2: int):
    """Can divide two numbers

    Args:
        num1 (int): no. 1
        num2 (int): no. 2
    """
    return num1 / num2
