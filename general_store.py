# Asking the user to select a profession and creating a variables to store budget for each profession
user_profession = input("Select a profession(Salesman, Uni student, or Trucker)? ") 
initial_balance_for_salesman = 1000.00
initial_balance_for_uni_student = 500.00
initial_balance_for_trucker = 200.00
# Initializing variables containing amount of desired items
amount_of_fried_chicken_legs = ""
amount_of_beef_burgers = ""
amoint_of_cans_of_coke = ""
amount_of_PCs = ""
amount_of_hockey_sticks = ""
amount_of_basketball_hoops = ""
# Listing out items for sale with the initial amount the user has, plus creating postcondition loop to repeatedly ask for amount of items for some budget
while True:
	print("         General Store       ")
	print("1. Food                 $0.00")
	print("2. Office supplies      $0.00")
	print("3. Sport equipment      $0.00")
	if user_profession == "Salesman": #Conditions for salesman
		print("Amount you have: " + str(initial_balance_for_salesman))
		choice1 = input("What would you like to buy (Type in the number associated with your desired supply)? ")
		if choice1 == "1":
			print("The general store is offering fried chicken legs, beef burgers, and a can of coke.\n Each fried chicken costs $2.00, each beef burger costs $4.00, and each can of coke costs $1.00.")
			amount_of_fried_chicken_legs = int(input("How many fried chicken legs do you want? "))
			amount_of_beef_burgers = int(input("How many beef burgers do you want? "))
			amount_of_cans_of_coke = int(input("How many cans of coke do you want? "))
			initial_balance_for_salesman = (float(initial_balance_for_salesman))-((2*amount_of_fried_chicken_legs) + (4*amount_of_beef_burgers) + (1*amount_of_cans_of_coke))
			if initial_balance_for_salesman < 0:
				print("You are out of money or cannot afford the cost.")
				break
		
		elif choice1 == "2":
			print("The general store is offering PCs and mac laptops. The PCs costs $100.00 each and the laptops costs $105.00 each.")
			amount_of_PCs = int(input("How many PCs do you want? "))
			amount_of_laptops = int(input("How many laptops do you want? "))
			initial_balance_for_salesman = ((float(initial_balance_for_salesman))-((100*amount_of_PCs) + (105*amount_of_laptops)))
			if initial_balance_for_salesman < 0:
				print("You are out of money or cannot afford the cost.")
				break
		
		elif choice1 == "3":
			print("The general store is offering a hockey stick and a basketball hoop. Hockey sticks cost $8.00 each and basketball hoops cost $50.00 each.")
			amount_of_hockey_sticks = int(input("How many hockey sticks do you want? "))
			amount_of_basketball_hoops = int(input("How many basketball hoops do you want? "))
			initial_balance_for_salesman = ((float(initial_balance_for_salesman))-((8*amount_of_hockey_sticks)+(50*amount_of_basketball_hoops)))
			if initial_balance_for_salesman < 0:
				print("You are out of money or cannot afford the cost.")
				break
	elif user_profession == "Uni Student": #conditions for uni student
		print("Amount you have: " + str(initial_balance_for_uni_student))
		choice1 = input("What would you like to buy (Type in the number associated with your desired supply)? ")
		if choice1 == "1":
			print("The general store is offering fried chicken legs, beef burgers, and a can of coke.\n Each fried chicken costs $2.00, each beef burger costs $4.00, and each can of coke costs $1.00.")
			amount_of_fried_chicken_legs = int(input("How many fried chicken legs do you want? "))
			amount_of_beef_burgers = int(input("How many beef burgers do you want? "))
			amount_of_cans_of_coke = int(input("How many cans of coke do you want? "))
			initial_balance_for_uni_student = (float(initial_balance_for_uni_student))-((2*amount_of_fried_chicken_legs) + (4*amount_of_beef_burgers) + (1*amount_of_cans_of_coke))
			if initial_balance_for_uni_student < 0:
				print("You are out of money or cannot afford the cost.")
				break
		elif choice1 == "2":
			print("The general store is offering PCs and mac laptops. The PCs costs $100.00 each and the laptops costs $105.00 each.")
			amount_of_PCs = int(input("How many PCs do you want? "))
			amount_of_laptops = int(input("How many laptops do you want? "))
			initial_balance_for_uni_student = ((float(initial_balance_for_uni_student))-((100*amount_of_PCs) + (105*amount_of_laptops)))
			if initial_balance_for_uni_student < 0:
				print("You are out of money or cannot afford the cost.")
				break
		elif choice1 == "3":
			print("The general store is offering a hockey stick and a basketball hoop. Hockey sticks cost $8.00 each and basketball hoops cost $50.00 each.")
			amount_of_hockey_sticks = int(input("How many hockey sticks do you want? "))
			amount_of_basketball_hoops = int(input("How many basketball hoops do you want? "))
			initial_balance_for_uni_student = ((float(initial_balance_for_uni_student))-((8*amount_of_hockey_sticks)+(50*amount_of_basketball_hoops)))
			if initial_balance_for_uni_student < 0:
				print("You are out of money or cannot afford the cost.")
				break
	else: #Conditions for trucker
		print("Amount you have: " + str(initial_balance_for_trucker)) 
		choice1 = input("What would you like to buy (Type in the number associated with your desired supply)? ")
		if choice1== "1":
			print("The general store is offering fried chicken legs, beef burgers, and a can of coke.\n Each fried chicken costs $2.00, each beef burger costs $4.00, and each can of coke costs $1.00.")
			amount_of_fried_chicken_legs = int(input("How many fried chicken legs do you want? "))
			amount_of_beef_burgers = int(input("How many beef burgers do you want? "))
			amount_of_cans_of_coke = int(input("How many cans of coke do you want? "))
			initial_balance_for_trucker = (float(initial_balance_for_trucker))-((2*amount_of_fried_chicken_legs) + (4*amount_of_beef_burgers) + (1*amount_of_cans_of_coke))
			if initial_balance_for_trucker < 0:
				print("You are out of money or cannot afford the cost.")
				break
		elif choice1 == "2":
			print("The general store is offering PCs and mac laptops. The PCs costs $100.00 each and the laptops costs $105.00 each.")
			amount_of_PCs = int(input("How many PCs do you want? "))
			amount_of_laptops = int(input("How many laptops do you want? "))
			initial_balance_for_trucker = ((float(initial_balance_for_trucker))-((100*amount_of_PCs) + (105*amount_of_laptops)))
			if initial_balance_for_trucker < 0:
				print("You are out of money or cannot afford the cost.")
				break
		elif choice1 == "3":
			print("The general store is offering a hockey stick and a basketball hoop. Hockey sticks cost $8.00 each and basketball hoops cost $50.00 each.")
			amount_of_hockey_sticks = int(input("How many hockey sticks do you want? "))
			amount_of_basketball_hoops = int(input("How many basketball hoops do you want? "))
			initial_balance_for_trucker = ((float(initial_balance_for_trucker))-((8*amount_of_hockey_sticks)+(50*amount_of_basketball_hoops)))
			if initial_balance_for_trucker < 0:
				print("You are out of money or cannot afford the cost.")
				break
		
				
		
			
				
			
			
				
			
