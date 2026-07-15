class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Substraction(self):
        Ans = self.No1 - self.No2
        return Ans

    def Multiplication(self):
        Ans = self.No1 * self.No2
        return Ans

    def Division(self):
        Ans = self.No1 / self.No2
        return Ans

value1 = int(input("Enter first number :"))
value2 = int(input("Enter second number :"))

Aobj = Arithmatic(value1,value2)

Ret = Aobj.Addition()
print("Addition is :",Ret)

Ret = Aobj.Substraction()
print("Substraction is :",Ret)

Ret = Aobj.Multiplication()
print("Multiplication is :",Ret)

Ret = Aobj.Division()
print("Division is :",Ret)