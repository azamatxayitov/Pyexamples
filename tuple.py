''''
Tuple
1 what is tuple: tuple vs list
2 unpacking arguments 
3 zip
'''

# literal 
numbs = [2, 4, 1, 4]

# constructor 
letters = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)

# we can not mutate tuple 
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"