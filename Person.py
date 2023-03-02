# This class represents a person, with attributes for a name and a social security number
class Person:
    def __init__(self, name, social_security_number, staff_member, has_supervisor,student):
        self.name = name
        self.social_security_number = social_security_number
        self.staff_member = staff_member
        self.has_supervisor = has_supervisor
    
    # This class represents person who is a staff member and has a supervisor
class Staff(Person):
    pass

case1 = Person()
    
# This subclass represents a person who is a student that takes courses at the university
class Student2(Person, Course, Loan, Student1):
    pass

case2 = Person()
case3 = Course()
case4 = Loan()
case5 = Student1()
