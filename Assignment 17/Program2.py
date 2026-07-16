class BankAccount:
    Roi = 10.5
    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name of account holder :",self.Name)
        print("Current balence :",self.Amount)

    def Diposit(self):
        print("Enter the amount that you want to add:")
        No = int(input())

        self.Amount += No

        print("the current balance will be :",self.Amount)

    def Withdraw(self):
        print("Enter withdraw Amount:")
        Value = int(input())

        if Value <= self.Amount:
            self.Amount = self.Amount - Value
            print("The remaining balence in your account is :",self.Amount)
        else:
            print("there are no sufficient balance in your account : Sorry")

    def ROI(self):
        Intrest = (self.Amount + BankAccount.Roi)/100
        return Intrest

obj1 = BankAccount("Prasad", 10000)
obj2 = BankAccount("Ayush", 20000)

obj1.Display()
obj1.Diposit()
obj1.Withdraw()
obj1.Display()
print("Interest:", obj1.ROI())

obj2.Display()
obj2.Diposit()
obj2.Withdraw()
obj2.Display()
print("Interest:", obj2.ROI())
