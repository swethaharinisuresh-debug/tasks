#users_list = []

#def create_user(name, age, role):

 #   Creates a user dictionary and returns it.
#    Formats the name using .title().
    
    
    #formatted_name = name.title()
    
   # user_dict = {
    #    "name": formatted_name,
     #   "age": age,
      #  "role": role
    #}
    
  #  return user_dict


#users_list.append(create_user("alice smith", 25, "Software Engineer"))
#users_list.append(create_user("BOB JOHNSON", 32, "Project Manager"))
#users_list.append(create_user("clara barton", 28, "Data Analyst"))

#print("--- Registered Users ---")
#for user in users_list:
 #   print(user)

#def calculate_total(*numbers):
 #   if not numbers:
  #      return 0, 0
    
   # total_sum = sum(numbers)
    #average = total_sum / len(numbers)
    
  #  return total_sum, average
#total, avg = calculate_total(10, 20, 30, 40, 50)

#print(f"Sum: {total}")
#print(f"Average: {avg}")

#def system_config(**settings):
 #   """
  ## """
    #for key, value in settings.items():
     #   print(f"{key}: {value}")
#system_config(mode="debug", version="1.0")

#def factorial(n):
    
 #   if n < 0:
  #      return "Error: Factorial is not defined for negative numbers."
   # if n == 0:
    #    return 1
    
    #else:
     #   return n * factorial(n - 1)
#print(f"Factorial of 5: {factorial(5)}")   
#print(f"Factorial of 0: {factorial(0)}")   
#print(f"Factorial of -1: {factorial(-1)}") 

#def square_generator(n):
 #   for i in range(n):
        
  #      yield i ** 2
#n = 5

#normal_list = [i**2 for i in range(n)]
#gen = square_generator(n)
#print(f"Normal list: {normal_list}")
#print(f"Type of normal list: {type(normal_list)}")

#print("\nGenerator values:", list(square_generator(n))) # Converting to list just to show values
#print(f"Type of generator: {type(gen)}")

#try:
 #   numerator = float(input("Enter numerator: "))
  ## result = numerator / denominator
    #print(f"Result: {result}")

#except ValueError:
  #  print("Error: Invalid input. Please enter numeric values.")

#except ZeroDivisionError:
 #   print("Error: Cannot divide by zero."

#filename = "team_data.txt"
#user_details = input("Enter the team details you want to save: ")

#with open(filename, "w") as file:
 ##  print(f"--- Data saved to {filename} ---")
#print("\nReading file content...")
#with open(filename, "r") as file:
 #   content = file.read()
  #  print(f"Content: {content}")
#if file.closed:
 #   print("\n[Bonus] Status: The file has been successfully closed.")
#else:
 #   print("\n[Bonus] Status: The file is still open.")