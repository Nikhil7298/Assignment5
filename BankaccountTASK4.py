class Account:
  def __init__(self,title,balance):
    self.title=title
    self.balance=balance
  def withdraw(self,w):
    return(self.balance-w)
  def deposit(self,d):
    return(self.balance+d)
  def getbalance(self):
    return(self.balance)
class savingsaccount(Account):
  def __init__ (self,title,balance,intrestrate):
    super().__init__(title,balance)
    self.intrestrate=intrestrate

  def intrestamount(self):
    return((self.intrestrate*self.balance)/100)
  
z=savingsaccount('Nikhil',5000,5)
print(z.intrestamount())