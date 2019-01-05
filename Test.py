import math

x = "Hello"
print(x)

for i in range(10):
    print("Printing " + i.__str__())

a = None
print(a is None)
print(5 == 6)
print(bool([]))
print(bool([1, 3, 7]))
print(math.factorial(100))
print("Length of the factorial 100 is " + len(str(math.factorial(100))).__str__())
print(bool(bool("False")))

if "eggs":
    print("Yes Please !! ")
else:
    print("Go to hel !! ")

counter = 5
while counter:
    print(counter)
    counter -= 1

while True:
    res = input()
    if int(res) % 5 == 0:
        break
