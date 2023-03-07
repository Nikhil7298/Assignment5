class student:
  def __init__ (self,name,rollnumber):
    self.name=name
    self.rollnumber=rollnumber
  def getname(self):
    return(self.name)
  def setname(self,name):
    self.name=name
  def getid(self):
    return(self.rollnumber)
  def setid(self,rollnumber):
    self.rollnumber=rollnumber
s=student('nikhil',903711)
name=s.getname()
id=s.getid()
print(name)
print(id)
s.setname('john')
s.setid(999999)
name=s.getname()
id=s.getid()
print(name)
print(id)