import sys


def convert(x):
    '''
    convert to an integer
    '''

    try:
        print("Input " + x.__str__())
        return int(x)
    except (ValueError, TypeError) as ex:
        print("Conversion Error :: {e} ".format(e=str(ex)), file=sys.stderr)
        ValueError()
        return -1


# if __name__ == '__main__':
#     convert("IND")


def sqrt(x):

    """ Compute square root using the method of Heron of Alexandria.

    Args:
        x: The number for which the squre root is to be completed.

    Returns:
        The square root of x.
        ValueError
    """

    guess = x
    i = 0
    if x < 0:
        raise ValueError("Cannot compute square root of negative number {num}".format(num=x))

    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    print(sqrt(9))
    try:
        print(sqrt(-1))
    except (ZeroDivisionError, ValueError) as zex:
        print("{e}".format(e=str(zex)), file=sys.stderr)
    print("Normal flow continues")


if __name__ == '__main__':
    main()
    # convert("IND")
