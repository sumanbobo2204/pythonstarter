import FunctionsImptn

a = "first" + " second"
print(a)

# __name__ is a built-in variable which evaluates to the name of the current module.
# Thus it can be used to check whether the current script is being run on its own or
# being imported somewhere else by combining it with if statement, as shown below.

if __name__ == "__main__":
    print(FunctionsImptn.even_or_odd(21))

# Mutiline String representation -->
multi_line_string = '''Hi this is
                    a multiple line string
                    i hope u understand
                    yeah!!!! -> this is a \' escape sequence.
                    '''

print(multi_line_string)

# String as a sequence of unicode codepoints -->>

string_sequence = "United KingDOm"
print(string_sequence[7])

# capitalization of strings -->>

print(string_sequence.capitalize())

# str are unicode codepoint default is UTF-8 we can use escape sequence to implement
# various other unicode sequences -->>

print("\xe5")
print("This is not UTF-8" + " ::  s\u00e5 h\u00f8re")

# bytes -->> sequence of bytes ::
b = b'Hey Jude'
print(b.split())
print(type(b.split()))

# encoding -->> converting a str to bytes
print("τoρνoς".encode('utf-8'))

# decoding -->> converting bytes to a str
print(b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-16'))
print(b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-8'))

# list -->> mutable sequence of objects ::

test_list = ["Hey Jude", "pink floyd", 1970, "Titanic"]
print(test_list[3])
test_list[3] = 1971
print(test_list)

# dict -->> mutable mapping of keys to values ::
a = {"bob": 100, "dan": 150, "Jack": "hello"}
print(a["Jack"])
a["bob"] = "Hey"
print(a["bob"])
print(a)

# we are using urllib library to hit an url and get the data .. ha h ah a lol
from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)

    print(story_words)










