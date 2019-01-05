from math import sqrt

words = "Why sometimes I have believed as many as six possible things before my breakfast".split()

result = [len(w) for w in words]
print(result)

country_to_capital = {"India":"Delhi","United Kingdom":"London","Brazil":"Brasilia"}
c = {capital:country for country,capital in country_to_capital.items()}
print(c)


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


square_root_of_primes = [sqrt(x) for x in range(101) if is_prime(x)]
# print(square_root_of_primes);


prime_square_divisors = {x*x: (1, x, x*x) for x in range(101) if is_prime(x)}
print(prime_square_divisors)


# Generator functions -->>
def math_gen(x, y):
    """

    :rtype: genrator object
    """
    print("Generator function starts")
    yield x + y
    yield x - y
    yield x * y
    yield x // y
    print("Generator function ends")


gen = math_gen(20, 5)
# print(next(gen))
generator_result = [g for g in gen if g % 5 == 0]
print(generator_result)

