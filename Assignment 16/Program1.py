class Demo:
    value = 0

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def fun(self):
        print("Inside fun")
        print(self.No1)
        print(self.No2)
        print(Demo.value)
        

    def gun(self):
        print("Inside gun")
        print(self.No1)
        print(self.No2)
        print(Demo.value)
    

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()
