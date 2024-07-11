# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> 
# >>> price + _        # In interactive mode, the last printed expression is assigned to the variable '_' ... ->not applicable in complier mode
# 113.0625
# >>> 
# >>> round(_, 2)
# 113.06


#python has inbuild constructors which are basically used for type convertion

# int(): Converts a value to an integer.
int("42")  # Output: 42

# float(): Converts a value to a floating-point number.
float("3.14")  # Output: 3.14

#complex(): Creates a complex number from real and imaginary parts.
complex(1, 2)  # Output: (1+2j)

# str(): Converts a value to a string.
str(123)  # Output: '123'

#list(): Converts an iterable to a list.
list("abc")  # Output: ['a', 'b', 'c']

#tuple(): Converts an iterable to a tuple.
tuple([1, 2, 3])  # Output: (1, 2, 3)

#dict(): Creates a dictionary.
dict(a=1, b=2)  # Output: {'a': 1, 'b': 2}

#set(): Converts an iterable to a set.
set([1, 2, 3, 3])  # Output: {1, 2, 3}

#frozenset(): Converts an iterable to an immutable set.
frozenset([1, 2, 3])  # Output: frozenset({1, 2, 3})

#bool(): Converts a value to a Boolean.
bool(0)  # Output: False

#bytes(): Creates a bytes object.
bytes("hello", "utf-8")  # Output: b'hello'

#bytearray(): Creates a mutable array of bytes.
bytearray("hello", "utf-8")  # Output: bytearray(b'hello')

#memoryview(): Creates a memory view object.
memoryview(bytearray("abc", "utf-8"))  # Output: <memory at 0x...>

#range(): Creates an immutable sequence of numbers.
range(5)  # Output: range(0, 5)

#slice(): Creates a slice object.
slice(1, 5, 2)  # Output: slice(1, 5, 2)
