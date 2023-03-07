class Account:
  def __init__(self,title,balance):
    self.title=title
    self.balance=balance
class savingsaccount(Account):
   def __init__ (self,title,balance,intrestrate):
     super().__init__(title,balance)
     self.intrestrate=intrestrate
   def details(self):
      return(self.title,self.balance,self.intrestrate)
z=savingsaccount('Ashish',5000,5)
print(z.details())