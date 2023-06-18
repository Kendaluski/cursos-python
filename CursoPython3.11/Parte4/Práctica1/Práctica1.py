# Object and Classes

# class firstClass:
#     # Class attributes
#     def __init__(self):
#         print("Attributes declared")
#     # Class methods
#     def msg(self):
#         print("First Message")
#     def msg2(self):
#         print("Second Message")

# test = firstClass()

# print(type(test.msg))
# test.msg2()

class secondClass:
    def __init__(self, num):
        self.num = num

    def numCheck(self):
        if self.num > 0:
            print("Positive")
        elif self.num < 0:
            print("Negative")
        else:
            print("Zero")
            
    def loop(self):
        while self.num <= 10:
            print(self.num)
            self.num += 1

test = secondClass(int(input("Enter a number: ")))
test.numCheck()
test.loop()