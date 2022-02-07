# Importing random library to access 'randint' function
import random
# Creating variable to hold secret number
secret_number = random.randint(1,100)
# Creating variable for the user to guess
guess = ""
# Creating variable to keep count of the user's guesses
guess_count = 0
while guess_count < 10 and guess != secret_number:
	guess = int(input("Guess a number between 1 to 100: "))
	guess_count += 1
	if guess < 1 or guess > 100:
		print("You must guess a number between 1 and 100 inclusive")
		break
	elif guess < secret_number:
		print("Higher!")
	elif guess > secret_number: 
		print("Lower!")
	
# The while loops breaks under two cases: When we guess the right number or when we are out of guesses	
if guess == secret_number:
	print("You win!")
elif guess_count >= 10:
	print("You are out of guesses. You lose!")	
	

