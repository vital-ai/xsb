class Person:
  def __init__(self, name, age, favorite_ice_cream=None):
    self.name = name
    self.age = age
    if favorite_ice_cream is None:
      favorite_ice_cream = 'chocolate'
    self.favorite_ice_cream = favorite_ice_cream

  def func0(self):
    return("Hello my name is " + self.name)

  def func1(self,myclass):
    return("Hello my name is " + self.name + " and I'm a " + myclass)

#p1 = Person("John", 36)
#p1.myfunc() 
