# All classes have a function is called "__init__" function which is always executed when object 
# is being initiated
"""
class Student:
    name ="Awais"
    def __init__(self):
        print(self)
        print("Adding a new student in a database..")
        
s1=Student()        



class Student:
    def __init__(self,fullname):  # self parameter is a reference  to the current instant of the 
        # class and is used to access variables belong to a class
        self.name=fullname
        print("Adding a new student in a databse..")
        
s1=Student("Awais") 
print(s1.name)       
s2=Student("Ali") 
print(s2.name)    
"""
   
class Student:
     
    def __init__(self,name,marks):  
      self.name=name
      self.marks=marks        
s1=Student("Awais",97) 
print(s1.name,s1.marks)       
s2=Student("Ali",95) 
print(s2.name,s2.marks)       