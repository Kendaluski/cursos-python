# Functions


def testfunction():
    print("Hello World!")

# testfunction()

# Recursive

def recursive(num):
    if num == 1:
        return 1
    else:
        return num * recursive(num - 1)

# Conditionals

def printNums(num):
    while num <= 10:
        print(num)
        num += 1
