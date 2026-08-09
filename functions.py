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