#class User:
 ##   def _init_(self):
  #      self.__user_name = ""
   #     self.__pwd = ""
    #def set_user(self, user_name, pwd):
     #   self.__user_name = user_name
      #  self.__pwd = pwd

#    def get_user(self):
    
 #       return self.__user_name
  #  def register(self):
   #     print(f"Registering user: {self.__user_name}")
    #def login(self):
     #   print(f"Logging in: {self.__user_name}")
#user1 = User()
#user1.set_user("john", "secure123")
#user1.register()
#user1.login()


#class User:
    #def register(self):
   #  def login(self):
 #       print("User logged in successfully.")
#class Student(User):
  #  def student_greet(self):
 #       print("Hello Student")
#class Faculty(User):
  #  def faculty_greet(self):
 #       print("Hello Faculty")
#class TempFaculty(Faculty):
  #       print("Hello Temp Faculty")
#student_obj = Student()
#temp_faculty_obj = TempFaculty()
#user_obj = User()
#print("--- Child accessing Parent methods ---")
#student_obj.register() 
#temp_faculty_obj.faculty_greet()
#temp_faculty_obj.login()
#print("\n--- Calling specific child methods ---")
#student_obj.student_greet()
#temp_faculty_obj.tempFaculty_greet()
#print("\n--- Parent access restriction ---")
#try:
 #   user_obj.student_greet()
#except AttributeError:
#    print("Error: Parent class 'User' cannot access child method 'student_greet'")


#class User:
 #   def greet(self):
  #      print("Welcome User")

#class Student(User):
 #   def greet(self):
  #      print("Welcome Student")
#class Faculty(User):
 #   def greet(self):
  #      print("Welcome Faculty")
#student = Student()
##faculty = Faculty()
#student.greet()  
#faculty.greet()


#class User:
 ###     return self

    #def login(self):
     #   print("logined") 
      #  return self
   # def greet(self):
    #    print("enjoy everyone")
     #   return self
#user = User()
#user.login().greet().register()


#class User:
    #users_count = 0
    #def _init_(self, username):
      #  self.__username = username
     #   User.users_count += 1
    #def login(self):
      #  print(f"{self.__username} logged in.")
     #   return self
    #def register(self):
     #   print(f"{self.__username} registered.")
    #    return self
   # def greet(self):
  #      print(f"Hello, I am a general user named {self.__username}.")
 #       return self
#class Student(User):
   #      print(f"Hi! I am a student.")
 #       return self
#class Faculty(User):
   # def greet(self):
  #      print(f"Greetings! I am a faculty member.")
 #       return self
#print(f"Initial User Count: {User.users_count}")
#student_user = Student("Alice")
#student_user.login().greet().register()
#faculty_user = Faculty("Dr. Smith")
#faculty_user.login().greet().register()
#print(f"Final User Count: {User.users_count}")
