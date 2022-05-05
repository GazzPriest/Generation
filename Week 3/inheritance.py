# Parent class
class Person:     
  def __init__(self, name, age):    
    self.name = name 
    self.age = age 
    
  def display(self): 
    print(self.name) 
    print(self.age) 
  
# Child class 
class Employee(Person):            
  def __init__(self, name, age, salary, title):
    super().__init__(name, age)  
    self.salary = salary
    self.title = title

