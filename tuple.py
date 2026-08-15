''''
Tuple
1 what is tuple: tuple vs list
2 unpacking arguments 
3 zip
'''

# literal 
# numbs = [2, 4, 1, 4]

# # constructor 
# letters = list("Hello World!")

# fruits = ["apple", "lemon", "banana", "kiwi"]
# print("before fruits:", fruits)

# fruits[2] = "melon"
# print("after fruits:", fruits)

# # we can not mutate tuple 
# animals = ("dog", "cat", "fish", "lion")
# tuple_obj = ("MIT", 100, True, None)

# print(animals[0])
# # animals[0] = "bird"


groups = ["MIT", "FLEx", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z) # list

# *args > tuple
def calculate(*args):
    print("*args > ", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}") 
    return total

# CALL
calculate(1, 7, 2, 3)
calculate(0, 2, 300)
calculate(5, 7)


# **kwargs > dictionary   

def introduce(**kwargs):
    print(f"the type (**kwargs) value: {type(kwargs)}")
    print(f"Hi i am {kwargs["name"]} and I am an {kwargs["age"]} years old!")
    
# CALL 
introduce(name="Justin", age=28)
introduce(name="Shawn", age= 38, single=True)    