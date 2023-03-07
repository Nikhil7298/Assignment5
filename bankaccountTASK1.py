class Account:
  def __init__(self,title,balance):
    self.title=title
    self.balance=balance
  def getbalance(self):
    return(self.balance)
z=Account('Nikhil',5000)
print(z.getbalance())