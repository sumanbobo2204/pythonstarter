import math


# Tuples (immutable heterogeneous collection)
def min_max(items):
    return min(items), max(items)


lower, upper = min_max([21, 33, 78, 8., 90, 7866, 656, 455, 3, 56])  # Tuple unpacking
print(lower, upper)
print(type(lower))

# Strings (str)
departure, _, arrival = "London:Edinburgh".partition(":")
print(arrival)

print("current position {lat} {long}".format(lat="60N", long="5E"))

print("Math constants : Pi={m.pi} e={m.e}".format(m=math))
print("Math constants : Pi={m.pi:.3f} e={m.e:.3f}".format(m=math))


# enumerate function yields(index, value) tuples.
p = ["HI", 7878, 90.9, b'Suman', 898, 67.7878787]

for x in enumerate(p):
    print(x)

for i, v in enumerate(p):
    print("i = {0} v = {1}".format(i, v))


aa1 = "Hey jude i want to hold your hand".split()
print(aa1[1:-1])  # slicing of list

# copying list only copying the value ie. object , not the references. --> Shallow copy.
ss = aa1.copy()
print(ss is aa1)
print(ss == aa1)

# Shallow repetition ..
q = [[-1, +1]] * 5
print(q)

q[1].append(-2)
print(q)

a = ' '.join(["Hey", "Jude", "I", "am", "the", "king"])
print(a)
print(a.split())

# dict --> Itself mutable --> keys are immutable and values are mutable.
names_and_ages = [('Bob', 23), ('Allice', 67.909099), ('Dan', -90), ('Stewart', "ENG")]
ax = dict(names_and_ages)
print(ax)
print(type(names_and_ages[1]))

# set --> unordered , unique , immutable ...
sm = set([1, 4, 5, 89, 90, "kiki", -34.678, 90, 89, 1, 1, 4, 4])
sm1 = {1, 4, 5, 89, 90, "kiki", -34.678}
print(sm)
print(sm1)
print(sm1.copy() == sm1)
print(sm1.copy() is sm1)

