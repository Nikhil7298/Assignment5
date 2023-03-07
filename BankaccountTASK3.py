class Account:
  def __init__(self,title,balance):
    self.title=title
    self.balance=balance
  def withdraw(self,w):
    return(self.balance-w)
z=Account('Nikhil',5000)
print(z.withdraw(500))