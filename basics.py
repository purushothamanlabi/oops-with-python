"""
PYTHON BASICS: DATA TYPES, CONTROL FLOW, FUNCTIONS, AND MORE
A comprehensive reference guide for basic Python concepts.
"""

import copy
from copy import deepcopy
from typing import List

# =================================================================
# 1. DATA TYPES
# =================================================================

# Numeric Types
a = 10
b = 10.5
c = 2 + 3j
print("int:", a, type(a))
print("float:", b, type(b))
print("complex:", c, type(c))

# Boolean
d = True
print("bool:", d, type(d))

# Sequences (String, List, Tuple)
e = "hello"
print("str:", e, type(e))

f = [1, 2, 3]  # List (Mutable)
print("list:", f, type(f))

g = (1, 2, 3)  # Tuple (Immutable)
print("tuple:", g, type(g))

# Sets & Dictionaries
i = {1, 2, 3}  # Set (Mutable)
print("set:", i, type(i))

j = frozenset([1, 2, 3])  # Frozenset (Immutable)
print("frozenset:", j, type(j))

k = {"name": "abi", "age": 22}  # Dictionary (Mapping)
print("dict:", k, type(k))

# Other Built-in Types
h = range(5)
print("range:", list(h), type(h))

o = None
print("NoneType:", o, type(o))


# =================================================================
# 2. CONTROL FLOW
# =================================================================

# If-Else Conditions
name = 1
if name == 1:
    print("condition")
else:
    print("else condition ")

# Loops (For, While)
# Python has one for loop, but we use it with list, string, range, dictionary, tuple, set, etc.
for data in f:
    if data == 3:
        break
    if data == 2:
        continue
    print(data)
    
# Switch (Match-Case) - Python 3.10+
match name:
    case 200:
        print("Status: OK")
    case 1:
        print("Status: Created")

# while True:
#     print("Infinite loop")

# Avoid variable shadowing built-ins
for num in range(8):
    print(num)


# =================================================================
# 3. FUNCTIONS & SCOPE
# =================================================================

# Function with Try-Except-Finally
def function(here):
    try:
        return f"this is return: {here}"
    except Exception as e:
        print(e)
    finally:
        print("final block executed")

print(function("abi"))

# Access and modify global variable
temp = 10
def modify_global():
    global temp
    temp = 20
    print(f"Inside func: {temp}")

print(f"Before func: {temp}")
modify_global()
print(f"After func: {temp}")


# =================================================================
# 4. DECORATORS
# =================================================================

def my_decorator(func):
    def wrapper():
        print("Before logic")
        func()
        print("After logic")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()   # equivalent to: say_hello = my_decorator(say_hello)


# =================================================================
# 5. LAMBDA FUNCTIONS & TYPING
# =================================================================

plus = lambda x, y: x + y
print(f"Lambda result: {plus(1, 3)}")

# Type hinting
nums: List[int] = [1, 2, 7, 3]
nums.sort(reverse=True)
print(f"Sorted list: {nums}")


# =================================================================
# 6. SHALLOW COPY VS DEEP COPY
# =================================================================

# Shallow Copy
a_list = [[1, 2], [3, 4]]
b_list = copy.copy(a_list)

b_list[0][0] = 100
print(f"Shallow Copy (Original affected): {a_list}")

# Deep Copy
a_list2 = [[1, 2], [3, 4]]
b_list2 = deepcopy(a_list2)

b_list2[0][0] = 100
print(f"Deep Copy (Original NOT affected): {a_list2}")


# =================================================================
# 7. ITERATORS
# =================================================================

nums_iter = [1, 2, 3]
it = iter(nums_iter)   # create iterator
# print(help(iter))

print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3


# =================================================================
# 8. *ARGS AND **KWARGS
# =================================================================

def func_args(*args):
    print(f"args (tuple): {args}")

func_args(1, 2, 3)

def func_kwargs(**kwargs):
    print(f"kwargs (dict): {kwargs}")

func_kwargs(name="Abi", age=22)

def func_both(*args, **kwargs):
    print(f"both: args={args}, kwargs={kwargs}")

func_both(1, 2, name="Abi", role="admin")

# =================================================================
# END OF NOTES
# =================================================================

