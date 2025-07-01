def PrintName():
    age = 30
    print("Age: " + str(age))  # Convert int to str for concatenation

def Add(num1, num2):
    return num1 + num2  # You probably meant addition, not multiplication

def SayHello():
    name = input("What is your name? ")  # Use input() correctly with a string prompt
    print("Hello", name)  # 'userName' is undefined, use 'name' instead

PrintName()
print(Add(5, 5))
SayHello()


