class SBI():
    def balinfo(self):
        self.sbal=40000
        print("current Balane=",self.sbal)
class Gpay(SBI):
    def gtransfer(self):
        amt=int(input("enter the Amount"))
        if(self.sbal>amt):
            self.sbal=self.sbal-amt
            print("amount debited succssfully")
            print("debited amount",amt)
            print("current balance",self.sbal)
        else:
            print("insufficent")

class phonepe(SBI):
    def phtrancefer(self):
        amt=int(input("enter the Amount"))
        if(self.sbal>amt):
            self.sbal=self.sbal-amt
            print("amount debited success")
            print("debited amount",amt)
            print("current balance",self.sbal)
        else:
            print("insufficient Balance")
    ch=int(input("1.Gpay\n2.phonepe\nselect one"))
    if(ch==1):
        g=Gpay()
        g.balinfo()
        g.gtransfer()
    elif(ch==2):
        ph=phonepe()
        ph.balinfo()
        ph.phtrancefer()
    else:
        print("invalid choice")