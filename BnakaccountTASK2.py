class Account:
  def __init__(self,title,balance):
    self.title=title
    self.balance=balance
  def deposit(self,d):
    return(self.balance+d)
z=Account('Nikhil',5000)
print(z.deposit(500))