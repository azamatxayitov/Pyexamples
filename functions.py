# build in function > print() type()
# function - reusable block of code!
# Instead of block {} in JAVA , Python uses indentation!

# Define - build
def greet(a):
    print(f"how do you do, {a}")
    
def greeting(b):
    print("greeting is executed")
    return f"hi {b}"

# Call - execute
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)   


##############################


# DEFINE
def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"

# CALL
result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

result4 = give_greet("John")
print("result4:", result4)