# This class represents a person, with attributes for a name and a social security number
class Person:
    def __init__(self, name, social_security_number):
        self.name = name
        self.social_security_number = social_security_number
    
    # This class represents person who is a staff member and has a supervisor
    def staff(self,staff_member):
        self.staff_member = staff_member
        