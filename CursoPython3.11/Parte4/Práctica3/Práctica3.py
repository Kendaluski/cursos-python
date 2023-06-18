# Potting

class pot:

    def __init__(self):
        self.__num = 0

    def add(self):
        print(self.__num + 10)
    
    def res(self):
        return self.__num
    
test = pot()
test.add()
test.__num = 20
print(test.res())
