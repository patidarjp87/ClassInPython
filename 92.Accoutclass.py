print("define a class Account with static variable rate of interest ,instance variable balance and accounr no.make function to set them")
class Account:
    def setAccount(self,a,b,rate):
        self.accno=a
        self.balance=b
        Account.roi=rate 
    def showBalance(self):
        print("Balance is ",self.balance)
    def showROI(self):
        print("rate of interest is",Account.roi)
    def showWithdraw(self,withdrawAmount):
        if withdrawAmount>self.balance:
            print("withdraw unsuccessful...!!! , your account does not have sufficient balance")
        else:
            print("your request has proceed successfully")
            self.balance-=withdrawAmount
    def showDeposite(self,Amount):
        self.balance+=Amount
        s=input("Case deposite successfully...!!! , Type yes to show balance otherwise no")
        if s=='yes':
            print("Your updated balance is ",self.balance)
acc=Account()
acc.setAccount(101,10000,2)
acc.showBalance()
acc.showROI()
withdrawAmount=eval(input('Enter withdraw amount'))
acc.showWithdraw(withdrawAmount)
Amount=eval(input('Enter a deposite amount'))
acc.showDeposite(Amount)
input()
