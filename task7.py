#class User:
   # def _init_(self, name, id):
  #      self.name = name
 #       self.id = id

#class Student(User):
    #def _init_(self, name, id, dept, fees):
   #     super()._init_(name, id)
  #      self.dept = dept
 #       self.fees = fees

#class Faculty(User):
   # def _init_(self, name, id, salary):
  #       self.salary = salary

#class TempFaculty(Faculty):
   # def _init_(self, name, id, salary, duration):
  #       self.duration = duration
#temp_staff =TempFaculty ("swetha", "F123", 50000, "6 months")
#print(f"Name: {temp_staff.name}, Salary: {temp_staff.salary}, Duration: {temp_staff.duration}")

#class abstractuser:
 #     def _init_(self, name, student_id):
  #      self.name = name
   #     self.student_id = student_id

    
    #  def get_details(self):
     #   return f"Student: {self.name} (ID: {self.student_id})"

#class abstractuser:
 #   def _init_(self, name, subject):
  #      self.name = name
   #     self.subject = subject
    #def get_details(self):
     #   return f"Teacher: {self.name}, Subject: {self.subject}"

#class Student:
    #def _init_(self, name, fees):
    #    self.name = name
   #     self.fees = fees
  #  def _repr_(self):
 #class Faculty:
    #def _init_(self, name, salary):
    #    self.name = name
   #     self.salary = salary

  #  def _repr_(self):
 #       return f"Faculty({self.name}, Salary: {self.salary})"
#students = [
   # Student("swetha",4000),
  #  Student("Bob", 3000),
 #   Student("Charlie", 4500)
#]

#faculties = [
  #  Faculty("Prof. Smith", 80000),
 #   Faculty("Dr. Jones", 95000),
#    Faculty("Prof. Lee", 72000)
#]
#students.sort(key=lambda x: x.fees)
#print("Students sorted by fees:", students)
#faculties.sort(key=lambda x: x.salary)
#print("Faculty sorted by salary:", faculties)

#names = list(map(lambda s: s.name, students))
#print(names)

#class Student:
 #   def _init_(self, name, age):
  #     self.age = age
#students = [
 #   Student("Alice", 20),
  #  Student("Bob", 22),
# Student("Charlie", 21)
#]
#names = list(map(lambda s: s.name, students))
#print(names)


#students = [
   # {'name': 'Alice', 'fees': 60000},
  #  {'name': 'Bob', 'fees': 45000},
 #   {'name': 'Charlie', 'fees': 75000}
#]
#faculty = [
   # {'name': 'Dr. Smith', 'salary': 50000},
  #  {'name': 'Prof. Jones', 'salary': 25000},
 #   {'name': 'Dr. Taylor', 'salary': 40000}
#]
# Get students with fees > 50000
#high_fee_students = list(filter(lambda s: int(s['fees']) > 50000, students))
#high_salary_faculty = list(filter(lambda f: int(f['salary']) > 30000, faculty))
#print("Students with fees > 50,000:", high_fee_students)
#print("Faculty with salary > 30,000:", high_salary_faculty)

#from functools import reduce

#class Faculty:
  #  def __init__(self, name, salary):
 #       self.name = name
#        self.salary = salary
#class Student:
  #  def __init__(self, name, fees):
 #       self.name = name
#        self.fees = fees  # Fees stored as string based on your example
#faculties = [Faculty("Dr. Smith", 75000), Faculty("Prof. Jones", 82000)]
#students = [Student("Alice", "5000"), Student("Bob", "4500")]
#total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)
#total_fees = reduce(lambda acc, s: acc + int(s.fees), students, 0)
#print(f"Total Faculty Salary: {total_salary}")
#print(f"Total Fees Collected: {total_fees}")


#def process_users(users, func):
    
    #return list(map(func, users))
#users_list = ["alice", "bob", "charlie"]
#uppercased = process_users(users_list, str.upper)
#print(f"Uppercased: {uppercased}") 
#name_lengths = process_users(users_list, lambda name: len(name))
#print(f"Name lengths: {name_lengths}") 

#from dataclasses import dataclass
#from functools import reduce

#@dataclass
#class Student:
   # name: str
  #  age: int
 #   fees: float
#  def get_details(self):
 #       return f"Student: {self.name}, Age: {self.age}, Fees: ${self.fees}"

#@dataclass
#class Faculty:
    # age: int
  #  salary: float

 #   def get_details(self):
#        return f"Faculty: {self.name}, Age: {self.age}, Salary: ${self.salary}"
#people = [
  #  Student("Alice", 20, 1500.0),
 #   Faculty("Dr. Smith", 45, 5000.0),
#    Student("Bob", 19, 1200.0),
#    Faculty("Prof. Jones", 50, 6000.0),
#    Student("Charlie", 22, 1800.0)
#]
#all_details = list(map(lambda p: p.get_details(), people))
#seniors = list(filter(lambda p: p.age > 25, people))
#sorted_people = sorted(people, key=lambda p: p.age)
#total_fees = reduce(lambda acc, p: acc + (p.fees if isinstance(p, Student) else 0), people, 0)
#total_salary = reduce(lambda acc, p: acc + (p.salary if isinstance(p, Faculty) else 0), people, 0)
#print("--- All Details (Map) ---")
#for d in all_details: print(d)
#print("\n--- Sorted Data (By Age) ---")
#for p in sorted_people: print(p.get_details())
#print("\n--- Filtered Data (Age > 25) ---")
#for p in seniors: print(p.get_details())
#print(f"\nTotal Fees: ${total_fees}")
#print(f"Total Salary: ${total_salary}")