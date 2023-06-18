# Hierarchy and Polymorphism

class father:
    def __init__(self, num):
        self.num = num
    def msg1(self):
        print("First Message")

    def msg2(self):
        print("Second Message")

    def msg3(self):
        print("Third Message")

class son(father):
    def __init__(self, num):
        super().__init__(num)

    def msg4(self):
        print("Fourth Message")
        print(self.num + 10)


test = son(int(input("Enter a number: ")))
test.msg1()
test.msg4()