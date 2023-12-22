class sex:
  def displayinfo(self):
    print("Hellow World")
class xxx(sex):
  def displayinfo(self):
    super().displayinfo()
    print("I Am PlayBoy")
obj=xxx()
obj.displayinfo()

#Here we use super() function whish is used for printing the data of parent class and it is defined in child class. Comment me the output of this code.............
