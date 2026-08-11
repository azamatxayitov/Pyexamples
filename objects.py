'''Objects 
1 what is object 
2 iterable objects & range
3 dictionary
4 error handling system
'''

import array # package/module
import math # package
from math import ceil
print("=== what is object ===")
# an object has state and method properties.
# everything is object in python!

print(type('hello world!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# paradigm > functional programming & OOP
# OOP 4 concepts > abstraction | inheritance | polymorphism
result1 = math.ceil(97.7) # call
print("result1:", result1)

result2 = ceil(98.7)
print("result2:, result2")