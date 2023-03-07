class Account:
  def __init__(self,title,balance):
    self.title=title
    self.balance=balance
  def details(self):
    return(self.title,self.balance)
z=Account('Ashish',5000)
print('Account holder name and balance : ',z.details())