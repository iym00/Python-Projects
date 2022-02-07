# Asking for the user's name, current year, and the year the user is born
user_name = input("What is your name? ")
current_year = int(input("What is the current year? "))
user_year_of_birth = int(input("What year were you born? "))
# Checking whether the user's birth year is a leap year
if (user_year_of_birth % 4 == 0 and user_year_of_birth % 100 != 0) or (user_year_of_birth % 4 == 0 and user_year_of_birth % 100 == 0 and user_year_of_birth % 400 == 0):
	print("You are either " + str((current_year - user_year_of_birth)-1) + " or " + str(current_year - user_year_of_birth) +  "  or " + str((current_year - user_year_of_birth)//4) + " years old.")

else:
	print("You are either " + str(current_year - user_year_of_birth) + " or " + str((current_year - user_year_of_birth)-1) + " years old.")	
	
	
