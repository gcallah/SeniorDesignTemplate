
"""
This Python module doesn't really do anything:
It exists just to show how we document our code in our code and how we connect
tests to the code.
"""


def some_func(x):
    """
    This function just exists to show how our tools can work with docstrings.
    It simply takes its argument `x` and prints it.
    """
    print(x)


def other_func(y):
    """
    **Even** inline documentation will sometimes get out of sync, like this:
    This function takes its two arguments, `x` and `y`, and multiplies them.
    """
    return y + 7


def main():
    """
    We'll start with a `main()` function that just returns an error code.
    """
    some_func(10)
    return 0


if __name__ == "__main__":
    main()
