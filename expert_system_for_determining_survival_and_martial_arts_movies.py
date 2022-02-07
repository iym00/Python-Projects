# Asking the user if he/she requires information on how the expert system will work
# Sub-genre1: Martial Arts
# "Way of the Dragon (1972)" -- martial art, Bruce Lee fights Chuck Norris, starring Bruce Lee
# "Kung Fu Panda (2008)" -- animated martial art, Po becomes dragon warrior, Starring Jack Black
# "Ip Man 3 (2015)" -- martial art, second sequel to a previous movie, Mike Tyson fight scene
# "Enter the dragon (1973)" -- martial art, released 1973, Starring Bruce Lee
# "TMNT (2007)" -- animated martial art, released 2007, 4 turtle main characters
# "Man of Tai Chi (2013)" -- martial art, released 2013, main character known as 'tiger'
# "Game of Death (1978)" -- martial art, released 1978, Starring Bruce Lee, Bruce Lee fights Kareem Abdul-Jabbar
# "Rush Hour 3 (2007)" -- martial art, released 2007, second sequel to 'Rush Hour'
# "Mortal Kombat (2021)" -- martial art, released 2021, violent (not child friendly)
# Sub-genre2: Survival
# "The Hunger Games (2012)" -- survival, female main character, main character has no children
# "After Earth (2013)" -- survival, released 2013, extraterrestrials conquer Earth, humans live outside of Earth
# "Jurassic Park 3 (2001)" -- survival, involves dinosaurs, Starring Alan Grant
# "The Quiet Place 2 (2021)" -- survival, female main character Emily Blunt, has children
# "The Purge (2013)" -- survival, released 2013, involves human crime
# "World War Z (2013)" -- survival, released 2013, involves zombie infection and not human crime
# "Alien (1979)" -- survival, released 1979, action takes place in outer space
# "Dinosaur (2000)" -- survival, involves dinosaurs, animated
# "The Great Wall (2017)" -- survival, involves green beasts, released 2017
# "Jurassic World (2015)" -- survival, involves dinosaurs, main character is Owen Grady, not Alan Grant
instructions = input("Welcome to the expert system.\nDo you require instructions to follow for this system (yes or no)? ")
if instructions == "yes":
# Creating precondition while loop to ensure the user understands how the system will work
	response_to_if_required_instructions = ""
	while response_to_if_required_instructions != "yes":
		response_to_if_required_instructions = input("The system will ask you to choose between two predefined sub-genres of movies, to which you will choose one and think of a movie within one of these two sub-genres, depending on the one you choose (if you chose survival, think of a survival movie, if you choose martial art, think of a martial arts movie). Then, a series of yes or no questions will be asked about the movie you are thinking of, to which you will answer yes or no. Finally, at the end, the system will 'guess' the movie which best matches your answers to the yes or no questions. Do you now understand the instructions to using this system (yes or no)? ")
	
	user_genre = input("Which of the two sub-genre would you like to consult? Maritial Arts or Survival? ") # Asking the user which sub-genre they want to consult
	if user_genre == "Martial Arts": # Creating if statements for when the user choices the sub-genre "Martial Arts" and with all the possible choices
		question1 = input("Is the movie's main character Bruce Lee (yes or no)? ")
		if question1 == "yes":
			question2 = input("Was the movie released in 1972 (yes or no)? ")
			if question2 == "yes":
				print("The movie is 'Way of the Dragon (1972)'.")
			
			else:
				question34 = input("Was the movie released in 1973 (yes or no)? ")
				if question34 == "yes":
					print("The movie is 'Enter the dragon (1973)'.?")
				else:
					print("The movie is 'Game of death (1978)'.")
		else:
			question4 = input("Is the movie's main character (or main characters) a animal (yes or no)? ")
			if question4 == "yes":
				question5 = input("Is the movie's main character a panda (yes or no)? ")
				if question5 == "yes":
					print("The movie is 'Kung fu Panda (2008)'.")
				else:
					print("The movie is 'TMNT (2007)'.")
			
			else:
				question99 = input("Is the main character of the movie known as 'tiger' (yes or no)? ")
				if question99 == "yes":
					print("The movie is 'Man of Tai Chi (2013)'.")
				else:
					question6 = input("Is the movie a second sequel to a previous movie (yes or no)? ")
					if question6 == "yes":
						question7 = input("Does the main character in the movie fight Mike Tyson at some part in the movie (yes or no)? ")
						if question7 == "yes":
							print("The movie is 'Ip Man 3 (2015)'.")
						
						else:
							print("The movie is 'Rush Hour 3 (2007)'.")
					else:
						question55 = input("Is the movie child friendly (yes or no)? ")
						if question55 == "yes":
							print("The movie is 'The Karate Kid (2010)'.")
						else:
							print("The movie is 'Mortal Kombat (2021)'.")
							
				
					
						
						
			
	
	else: # Creating if statements for when the user choices the sub-genre "Survival" and all the possible choices
		question43 = input("Is the main character of the movie a female (yes or no)? ")
		if question43 == "yes":
			question31 = input("Does the movie's main charaacter have children (yes or no)? ")
			if question31 == "yes":
				print("The movie is 'The Quiet Place 2 (2021)'.")
			else:
				print("The movie is 'The Hunger Games (2012)'")
		
		else:
			question81 = input("Are humans, in the movie, living on another planet due to extraterrestrials (yes or no)? ")
			if question81 == "yes":
				print("The movie is 'After Earth (2013)'.")
			else:
				question00 = input("Does the movie contain dinosaurs (yes or no)? ")
				if question00 == "yes":
					question01 = input("Are the dinosaurs animated (yes or no)? ")
					if question01 == "yes":
						print("The movie is 'Dinosaur (2000)'.")
					else:
						question02 = input("Is the main character of the movie Alan Grant? ")
						if question02 == "yes":
							print("The movie is 'Jurassic Park 3 (2001)'.")
						else:
							print("The movie is 'Jurassic world (2015)'.")
				
				else:
					question200 = input("Does the movie contain swarms of green beasts (yes or no)? ")
					if question200 == "yes":
						print("The movie is 'The Great Wall (2017)'.")
					else:
						question09 = input("Does most of the action in the movie take place in space (yes or no)? ")
						if question09 == "yes":
							print("The movie is 'Alien (1979)'.")
						else:
							question871 = input("Does the movie involve human crime (yes or no)? ")
							if question871 == "yes":
								print("The movie is 'The Purge (2013)'.")
							else:
								print("The movie is 'World War Z (2013)'.")
								
				
		
				
			
					

else: # Contains all the previous code when the user does not require instructions, since previous code is under if instructions == "yes" only
	user_genre = input("Which of the two sub-genre would you like to consult? Maritial Arts or Survival?")
	if user_genre == "Martial Arts":
		question1 = input("Is the movie's main character Bruce Lee (yes or no)? ")
		if question1 == "yes":
			question2 = input("Was the movie released in 1972 (yes or no)? ")
			if question2 == "yes":
				print("The movie is 'Way of the Dragon (1972)'.")
			
			else:
				question34 = input("Was the movie released in 1973 (yes or no)? ")
				if question34 == "yes":
					print("The movie is 'Enter the dragon (1973)'.?")
				else:
					print("The movie is 'Game of death (1978)'.")
		else:
			question4 = input("Is the movie's main character (or main characters) a animal (yes or no)? ")
			if question4 == "yes":
				question5 = input("Is the movie's main character a panda (yes or no)? ")
				if question5 == "yes":
					print("The movie is 'Kung fu Panda (2008)'.")
				else:
					print("The movie is 'TMNT (2007)'.")
			
			else:
				question99 = input("Is the main character of the movie known as 'tiger' (yes or no)? ")
				if question99 == "yes":
					print("The movie is 'Man of Tai Chi (2013)'.")
				else:
					question6 = input("Is the movie a second sequel to a previous movie (yes or no)? ")
					if question6 == "yes":
						question7 = input("Does the main character in the movie fight Mike Tyson at some part in the movie (yes or no)? ")
						if question7 == "yes":
							print("The movie is 'Ip Man 3 (2015)'.")
						
						else:
							print("The movie is 'Rush Hour 3 (2007)'.")
					else:
						question55 = input("Is the movie child friendly (yes or no)? ")
						if question55 == "yes":
							print("The movie is 'The Karate Kid (2010)'.")
						else:
							print("The movie is 'Mortal Kombat (2021)'.")
							
				
					
						
						
			
	
	else:	
		question43 = input("Is the main character of the movie a female (yes or no)? ")
		if question43 == "yes":
			question31 = input("Does the movie's main charaacter have children (yes or no)? ")
			if question31 == "yes":
				print("The movie is 'The Quiet Place 2 (2021)'.")
			else:
				print("The movie is 'The Hunger Games (2012)'")
		
		else:
			question81 = input("Are humans, in the movie, living on another planet due to extraterrestrials (yes or no)? ")
			if question81 == "yes":
				print("The movie is 'After Earth (2013)'.")
			else:
				question00 = input("Does the movie contain dinosaurs (yes or no)? ")
				if question00 == "yes":
					question01 = input("Are the dinosaurs animated (yes or no)? ")
					if question01 == "yes":
						print("The movie is 'Dinosaur (2000)'.")
					else:
						question02 = input("Is the main character of the movie Alan Grant? ")
						if question02 == "yes":
							print("The movie is 'Jurassic Park 3 (2001)'.")
						else:
							print("The movie is 'Jurassic world (2015)'.")
				
				else:
					question200 = input("Does the movie contain swarms of green beasts (yes or no)? ")
					if question200 == "yes":
						print("The movie is 'The Great Wall (2017)'.")
					else:
						question09 = input("Does most of the action in the movie take place in space (yes or no)? ")
						if question09 == "yes":
							print("The movie is 'Alien (1979)'.")
						else:
							question871 = input("Does the movie involve human crime (yes or no)? ")
							if question871 == "yes":
								print("The movie is 'The Purge (2013)'.")
							else:
								print("The movie is 'World War Z (2013)'.")
								
				
	
		
	
	
	


	
