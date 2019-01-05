m = [1, 2, 3, 56]
n = [1, 2, 3, 56]
ss = (34, 67, 78, 90)


def modify(x, xx=39):
    x.append(xx)
    print("x = ", x)


def replace(x1):
    x1 = [78, 89, 565]
    print("x1 = ", x1)


# Here the reference m pointing to the object , that object is modified by the method .
modify(m, 23)
print(m)
modify([])

# The reference n is still pointing to the old object here .
replace(n)
print(n)


def banner(message, border="."):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Hi This is a Banner")


def add_spam(mx=[]):
    mx.append("spam")
    print(mx)


def add_spam_modified(mx=[]):
    if mx is not None:
        mx=[ ]
        mx.append("spam")
        print(mx)


#add_spam()
#add_spam()
#add_spam()

add_spam_modified()
add_spam_modified()
add_spam_modified()

