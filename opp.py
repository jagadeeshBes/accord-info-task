class acbalance():
    def bal(self):
        self.balance=20000
class account1(acbalance):
    def currentac(self):
        amt1=int(input("Enter deposit amount"))
        self.dep=self.balance+amt1
        print("current blance",self.dep)
    def widthdraw(acbalance):
        amt2=int(input("enter withdraw amount"))
        if(self.balance>self.amt2):
            self.withd=self.balance-amt2
        else:
            print("insufficent balance")


class account2(acbalance):
    def savingac(self):
         amt=int(input("enter withdraw amount"))
         if(self.balance>self.amt):
             self.withd=self.balance-amt
             print("account balance",self.withd)
         else:
            print("insufficent balance")
    def simple(self):
        p=int(input("enter your amount"))
        r=float(input("enter your rate"))
        t=int(input("how many years"))
        self.value=p+(1+r)**t-p
        print("simple interest",self.value)

ch=int(input("1. current account\n2.saving acount"))
if(ch==1):
    ch1=int(input("1. deposit \n2. withdraw"))
    if(ch1==2):
        currt=account1()
        currt.bal()
        currt.widthdraw()
    elif ch1 == 1:
        cut=account1()
        cut.bal()
        cut.currentac()
elif(ch==2):
    ch2=int(input("1. wirrhdraw\n2. simple interest"))
    if(ch2==1):
        save=account2()
        saveing.bal()
        save.savingac()
    elif(ch2==2):
        saveing=account2()
        saveing.bal()
        saveing.simple()



    


        

    