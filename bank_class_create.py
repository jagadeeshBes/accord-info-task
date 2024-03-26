
class trf():
    def __init__(self):
        self.bankbal=20000
    def deposit(self):
        self.amt=int(input("enter deposit amount"))
        self.bankbal=self.bankbal+self.amt
        print("current bank blance",self.bankbal)
        print("deposit succssfull")
    
    def withdraw(self):
        self.amt=int(input("enter withdraw amount"))
        if(self.bankbal>self.amt):
            self.bankbal=self.bankbal-self.amt
            print("enter current blance",self.bankbal)
        else:
            print("insufficent blance")

bank=trf()
ch = int(input("1. bank blance\n2. deposit\n 3. withdraw\n"))
if(ch == 1):
    bank.bal()
elif(ch == 2):
    bank.deposit()
elif(ch == 3):
    bank.withdraw()
else:
    print("invalid choice")
    