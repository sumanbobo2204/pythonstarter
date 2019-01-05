import sys


def even_or_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("Odd")

# __name__ is a built-in variable which evaluates to the name of the current module.
# Thus it can be used to check whether the current script is being run on its own or
# being imported somewhere else by combining it with if statement, as shown below.


if __name__ == "__main__":
    print("Self running")
    print(even_or_odd(26))
else:
    print("imported!! ha ha ha !!")

from urllib.request import urlopen

# 'http://sixty-north.com/c/t.txt'


def fetch_words(url):
    """Fetch a list of words from a url

    Args:
        url: The url of a UTF-8 text document

    Returns:
        A list of string containing the words from the
        document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main():
    # sys.argv[0] is the module name that is executed..
    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)
    print_items([1, 2, 3, 4, 5, 6])


# invoking the main method
if __name__ == "__main__":
    main()
