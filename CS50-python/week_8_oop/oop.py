"""
# first writing style 
def main():
    student = get_student()
    print(student)
    


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house
    # return a tuple


if __name__ == "__main__":
    main()

"""

"""
# Class in python code

class Student:
    pass
# declare a class, a customized data type 


def get_student():
    student = Student()
    # declare an instance/ object from class Student
    
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
    # return the object 

def main():
    student = get_student()
    print(f"Name: {student.name}, House: {student.house}")
    

if __name__ == "__main__":
    main()
"""


# Class in python code

class Student:
   greeting = "hello"
   # global property for this class and unable access for its instance   
   def __init__(self, name, house):
      self.name = name
      self.house = house
      
      # declare a class,  writing its own property and methods
      # __init__ for class's instance to access via self keyword       


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    # declare an instance with paras
   
    return student
    # return the object 

def main():
    student = get_student()
    print(f"Name: {student.name}, House: {student.house}")
    print(f"{student.name} is from  House of  {student.house}")
    

if __name__ == "__main__":
    main()