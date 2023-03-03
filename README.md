# OOP
## Section 1 Assignment overview
The main concept is to implement classes that represent an in-memory "school database". There are eight classes you must implement: Course, Catalog, Semester, Loan, Person, Staff, Student and StudentAccount. Each class has its own purpose which will be explained below. You will also implement a standslone function that will help transform a Person into a student.
- Course       (no dependencies)
     - Represent a course with attributes for id, name and number of credits.
- Catalog  (Course class must be implemented)
     - Stores a collection of Course objects through a dictionary, usin g id as the key.
-  Semester     (Course class must be implemented)
     - Stores a collection of Course objects taken together
- Loan              (no dependencies)
     - Represents an amount of money, with attributes for id and the loan amount.
- StudentAccount                (Student class must be implemented)
     - Represents the fianancial status of a student.
- Person                  (no dependencies)
     - Represents a person, with attributes for a name and social security number.
- Staff(subclass of Person)              (Person class must be implemented)
     - Represents a person who is a staff member and has a supervisor.
- Student(subclass of Person)       (All classes must be implemented)
     - Represents a person who is a student that takes courses at the university.
