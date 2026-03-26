##print (user)

#user1={"name" : "velu","age" : 26,"role" : "general manager","salary" : 50000}
#user2={"name" : "kumar","age" : 27,"role" : "sales manager","salary" : 44000}
#user3={"name" : "ramesh","age" : 23,"role" : "sales officer","salary" : 30000}
#user4={"name" : "rajashree","age" : 25,"role" : "marketing manager","salary" : 40000}
#user_list=[]
#user_list.append (user)
#user_list.append (user1)
#user_list.append (user2)
#user_list.append (user3)
#user_list.append (user4)
#print(user_list)

#user["age"]=26
#rint (user)

#del user["role"]
#print(user)

#print (user_list)

#mini project2

#def calculate_grade(average):
    
 ### elif average >= 80:
    #    return "A"
###  elif average >= 60:
   #     return "C"
    #else:
     #   return "D/Fail"

#def display_report_card(student_dict):
    
 #   name = student_dict["name"]
  #  marks = student_dict["marks"]
    
    # Calculate Total and Average
   # total = sum(marks)
    #average = total / len(marks)
 #   grade = calculate_grade(average)
    
    # Formatting the Output
  #  print("-" * 30)
   # print(f"{'STUDENT REPORT CARD':^30}")
#    print("-" * 30)
 #   print(f"Student Name : {name}")
  #  print(f"Subject 1    : {marks[0]}")
   # print(f"Subject 2    : {marks[1]}")
   # print(f"Subject 3    : {marks[2]}")
 #   print("-" * 30)
  #  print(f"Total Marks  : {total}/300")
   # print(f"Average      : {average:.2f}")
    #print(f"Final Grade  : {grade}")
    #print("-" * 30)

# 1. Store data in a dictionary
#student_name = input("Enter student name: ")
#m1 = int(input("Enter marks for Subject 1: "))
#m2 = int(input("Enter marks for Subject 2: "))
#m3 = int(input("Enter marks for Subject 3: "))

#student_data = {
 #   "name": student_name,
  #  "marks": [m1, m2, m3]


# 2. Generate the report
#display_report_card(student_data)

#mini project3


#shopping_cart = []

#def add_product(name, price, quantity):
    # Requirement: Add products (name, price, quantity)
    # Each product is a dictionary stored inside the list
    #product = {
   #     "name": name,
  #      "price": price,
 #       "quantity": quantity}
    
  #  shopping_cart.append(product)
 #   print(f"Added {quantity}x {name} to the cart.")

#def calculate_total():
    # Requirement: Calculate total bill
   #  for item in shopping_cart:
  #      total += item["price"] * item["quantity"]
 #   return total

#def remove_item(product_name):
    
   # for item in shopping_cart:
     #        shopping_cart.remove(item)
   #         print(f"Removed {product_name} from the cart.")
  #          return
 #   print(f"Item '{product_name}' not found in cart.")

#def display_cart():
    
    #print("\n--- Current Shopping Cart ---")
   # if not shopping_cart:
     #   print("Your cart is empty.")
    #else:
        #print(f"{'Product':<15} | {'Price':<10} | {'Qty':<5} | {'Subtotal'}")
       # print("-" * 50)
      #  for item in shopping_cart:
     #       subtotal = item["price"] * item["quantity"]
   ##       print(f"TOTAL BILL: ${calculate_total():.2f}\n")

# --- Example Usage ---
#add_product("Laptop", 1200.00, 1)
#add_product("Mouse", 25.50, 2)
#display_cart()

#remove_item("Mouse")
#display_cart()
     
##user_db = {
  #  "SWETHA": "password123",
   ##"DEVI": "coding_is_fun"
#}


#print("--- Login System ---")
#input_username = input("Enter username: ")
#input_password = input("Enter password: ")


#if input_username in user_db:
    
 #   if user_db[input_username] == input_password:
        
  #      print(f"\n✅ Login Successful! Welcome back, {input_username}.")
   # else:
        
    #    print("\n❌ Login Failed: Incorrect password.")
#else:
    
 #   print("\n❌ Login Failed: Username does not exist.")

#name={"swetha","devi","suresh","kumar","raja","rani"}
#print(set(name))

#name="swetha"
#product="phone"

#print(name+ " manufactoring " + product + " products ")

#print("***{}***".format(name))
#print("{}***".format(name))
#print("***{}".format(name))

#accounts = {}

##   if name in accounts:
  #      print(f"Error: Account for {name} already exists.")
   # else:
    #    accounts[name] = initial_balance
     #   print(f"Account created for {name} with ${initial_balance}.")

##   if name in accounts:
  #      accounts[name] += amount
   #     print(f"${amount} deposited. New balance: ${accounts[name]}")
  #  else:
   #     print("Error: Account not found.")

##   if name in accounts:
  #      if amount <= accounts[name]:
   ##        print(f"${amount} withdrawn. Remaining balance: ${accounts[name]}")
     #   else:
      #      print("Error: Insufficient funds.")
#    else:
 #       print("Error: Account not found.")

#def check_balance(name):
 #   if name in accounts:
  #      print(f"Account: {name} | Balance: ${accounts[name]}")
   # else:
    #    print("Error: Account not found.")


#create_account("Alice", 500)
#deposit("Alice", 150)
#withdraw("Alice", 100)
#check_balance("Alice")

#votes = {}


#def add_candidate(name):
 #   if name not in votes:
  #      votes[name] = 0


#while True:
  #  action = input("Enter candidate name to vote (or 'done' to finish): ").strip()
 #   if action.lower() == 'done':
  #      break
    
    
   # add_candidate(action)
    #votes[action] += 1


#if votes:
 #   winner = max(votes, key=votes.get)
  #  print("\n--- Results ---")
   # for name, count in votes.items():
    #    print(f"{name}: {count} votes")
 #   print(f"\nWinner: {winner} with {votes[winner]} votes!")
#else:
#    print("No votes recorded.")


#Eenrollment_system = {}

#def add_student(name, courses):
 ### print(f"Added {name} with courses: {', '.join(courses)}")

#def update_courses(name, new_courses):
  #  """Adds additional courses to an existing student's list."""
 #   if name in enrollment_system:
  #      enrollment_system[name].extend(new_courses)
   #     print(f"Updated courses for {name}.")
    #else:
     #   print(f"Error: Student '{name}' not found.")

##   """Prints all students and their enrolled courses."""
  #  print("\n--- Current Enrollment Details ---")
   # if not enrollment_system:
    #    print("No students enrolled.")
    #for name, courses in enrollment_system.items():
     #   print(f"Student: {name:10} | Courses: {', '.join(courses)}")
    #print("----------------------------------\n")


#add_student("Alice", ["Python 101", "Data Science"])
#add_student("Bob", ["Web Dev"])

#display_details()


#update_courses("Bob", ["JavaScript", "CSS"])

#display_details()

def display_number_conversions(n):
    
    
    print(f"--- Results for Number: {n} ---")
    
    
    
    print(f"Binary:      {n:b}")
    print(f"Octal:       {n:o}")
    print(f"Hexadecimal: {n:x}")
    
    
    
    print(f"Formatted:   {n:,}")
    
    
    print(f"Scientific:  {n:e}")
    print("-" * 30)


try:
    user_num = int(input("Enter an integer to process: "))
    display_number_conversions(user_num)
except ValueError:
    print("Please enter a valid integer.")