print('abs: ', abs(-100))
# Returns True if all items in an iterable object are true
print("all:", all(list(range(1, 100))))

# Returns True if any item in an iterable object is true
print("any:", any(list(range(0, 10))))

# The ascii() function will replace any non-ascii characters with escape characters:
# å will be replaced with \xe5.
print("Ascii", ascii("My name is Ståle"))
print(bin(10))
print(bool(0))
print(bytearray(9))
print(bytes(9))


def x():
    a = 5


print(callable(x))
print(chr(425))
print(complex(1, 10))


class Person:
    name = "John"
    age = 36
    country = "Norway"


delattr(Person, 'age')

x = dict(name="John", age=36, country="Norway")
print(x)
x = divmod(89, 3) # *(29, 2)
print(x)

print(list(enumerate(tuple(range(0, 10)))))
