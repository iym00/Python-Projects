# Function for replacement
def replace(original_string, part_want_replaced, new_string):
	new_string_after_replacement = ""
	if part_want_replaced in original_string:
		a = original_string.index(part_want_replaced)
		if len(part_want_replaced) > len(new_string):
			first_part_of_string = original_string[:a]
			second_part_of_string = original_string[a+len(part_want_replaced):len(original_string)]
			new_string_after_replacement += first_part_of_string + new_string + second_part_of_string
			return new_string_after_replacement
		
		else:
			
			for i in range(len(original_string)):
				c = original_string.index(part_want_replaced)
				if i == c:
					new_string_after_replacement += new_string
					if ((i-1)+(len(new_string)+1)) > len(original_string):
						break
					
					else:
						i += (i-1) + (len(new_string) + 1)
				
				elif original_string[i] == part_want_replaced:
					new_string_after_replacement += new_string
					if ((i-1)+(len(new_string)+1)) > len(original_string):
						break
					
					else:
						i += (i-1) + (len(new_string) + 1)
						
				
				else:
					new_string_after_replacement += original_string[i]
				
			
			return new_string_after_replacement
					
		
				
	else:
		return "The part you want replaced doesn't exist in the original string."
	 
	
# Function replacing lower case letters to upper case letters
def lower_to_upper(string):
	new_string = ""
	for i in range(len(string)):
		if ord(string[i]) == ord(string[i].lower()):
			new_string += chr(ord(string[i].upper()))
		else:
			new_string += chr(ord(string[i]))
	
	return new_string

def phrase_to_acronym(string):
	if "BY THE WAY" not in string and "LAUGH OUT LOUD" not in string and "WHAT DO YOU MEAN" not in string and "TALK TO YOU LATER" not in string:
		return string
	
	elif "BY THE WAY" in string and "LAUGH OUT LOUD" not in string and "WHAT DO YOU MEAN" not in string and "TALK TO YOU LATER" not in string:
		string_with_acronym1 = replace(string, "BY THE WAY", "BTW")
		return string_with_acronym1
	
	elif "BY THE WAY" not in string and "LAUGH OUT LOUD" in string and "WHAT DO YOU MEAN" not in string and "TALK TO YOU LATER" not in string:
		string_with_acronym2 = replace(string, "LAUGH OUT LOUD", "LOL")
		return string_with_acronym2
	
	elif "BY THE WAY" not in string and "LAUGH OUT LOUD" not in string and "WHAT DO YOU MEAN" in string and "TALK TO YOU LATER" not in string:
		string_with_acronym3 = replace(string, "WHAT DO YOU MEAN", "WDYM")
		return string_with_acronym3
	
	elif "BY THE WAY" not in string and "LAUGH OUT LOUD" not in string and "WHAT DO YOU MEAN" not in string and "TALK TO YOU LATER" in string:
		string_with_acronym4 = replace(string, "TALK TO YOU LATER", "TTYL")
		return string_with_acronym4
	
	elif "BY THE WAY" in string and "LAUGH OUT LOUD" in string and "WHAT DO YOU MEAN" not in string and "TALK TO YOU LATER" not in string:
		string_with_acronym1 = replace(string, "BY THE WAY", "BTW")
		string_with_acronym2 = replace(string_with_acronym1, "LAUGH OUT LOUD", "LOL")
		return string_with_acronym2
	
	elif "BY THE WAY" in string and "LAUGH OUT LOUD" not in string and "WHAT DO YOU MEAN" in string and "TALK TO YOU LATER" not in string:
		string_with_acronym1 = replace(string, "BY THE WAY", "BTW")
		string_with_acronym3 = replace(string_with_acronym1, "WHAT DO YOU MEAN", "WDYM")
		return string_with_acronym3
	
	elif "BY THE WAY" in string and "LAUGH OUT LOUD" not in string and "WHAT DO YOU MEAN" not in string and "TALK TO YOU LATER" in string:
		string_with_acronym1 = replace(string, "BY THE WAY", "BTW")
		string_with_acronym4 = replace(string_with_acronym1, "TALK TO YOU LATER", "TTYL")
		return string_with_acronym4
	
	elif "BY THE WAY" not in string and "LAUGH OUT LOUD" in string and "WHAT DO YOU MEAN" in string and "TALK TO YOU LATER" not in string:
		string_with_acronym2 = replace(string, "LAUGH OUT LOUD", "LOL")
		string_with_acronym3 = replace(string_with_acronym2, "WHAT DO YOU MEAN", "WDYM")
		return string_with_acronym3
	
	elif "BY THE WAY" not in string and "LAUGH OUT LOUD" in string and "WHAT DO YOU MEAN" not in string and "TALK TO YOU LATER" in string:
		string_with_acronym2 = replace(string, "LAUGH OUT LOUD", "LOL")
		string_with_acronym4 = replace(string_with_acronym2, "TALK TO YOU LATER", "TTYL")
		return string_with_acronym4
	
	elif "BY THE WAY" not in string and "LAUGH OUT LOUD" not in string and "WHAT DO YOU MEAN" in string and "TALK TO YOU LATER" in string:
		string_with_acronym3 = replace(string, "WHAT DO YOU MEAN", "WDYM")
		string_with_acronym4 = replace(string_with_acronym3, "TALK TO YOU LATER", "TTYL")
		return string_with_acronym4
		
	elif "BY THE WAY" in string and "LAUGH OUT LOUD" in string and "WHAT DO YOU MEAN" in string and "TALK TO YOU LATER" not in string:
		string_with_acronym1 = replace(string, "BY THE WAY", "BTW")
		string_with_acronym2 = replace(string_with_acronym1, "LAUGH OUT LOUD", "LOL")
		string_with_acronym3 = replace(string_with_acronym2, "WHAT DO YOU MEAN", "WDYM")
		return string_with_acronym3
	
	elif "BY THE WAY" in string and "LAUGH OUT LOUD" not in string and "WHAT DO YOU MEAN" in string and "TALK TO YOU LATER" in string:
		string_with_acronym1 = replace(string, "BY THE WAY", "BTW")
		string_with_acronym3 = replace(string_with_acronym1, "WHAT DO YOU MEAN", "WDYM")
		string_with_acronym4 = replace(string_with_acronym3, "TALK TO YOU LATER", "TTYL")
		return string_with_acronym4
	
	elif "BY THE WAY" not in string and "LAUGH OUT LOUD" in string and "WHAT DO YOU MEAN" in string and "TALK TO YOU LATER" in string:
		string_with_acronym2 = replace(string, "LAUGH OUT LOUD", "LOL")
		string_with_acronym3 = replace(string_with_acronym2, "WHAT DO YOU MEAN", "WDYM")
		string_with_acronym4 = replace(string_with_acronym3, "TALK TO YOU LATER", "TTYL")
		return string_with_acronym4
	
	elif "BY THE WAY" in string and "LAUGH OUT LOUD" in string and "WHAT DO YOU MEAN" in string and "TALK TO YOU LATER" in string:
		string_with_acronym1 = replace(string, "BY THE WAY", "BTW")
		string_with_acronym2 = replace(string_with_acronym1, "LAUGH OUT LOUD", "LOL")
		string_with_acronym3 = replace(string_with_acronym2, "WHAT DO YOU MEAN", "WDYM")
		string_with_acronym4 = replace(string_with_acronym3, "TALK TO YOU LATER", "TTYL")
		return string_with_acronym4
	

def letter_to_homoglyph(string):
	if "A" not in string and "B" not in string and "K" not in string and "H" not in string:
		return string
	
	elif "A" in string and "B" not in string and "K" not in string and "H" not in string: 
		stringer1 = replace(string, "A", "@")
		return stringer1
	
	elif "A" not in string and "B" in string and "K" not in string and "H" not in string:
		stringer2 = replace(string, "B", "|3")
		return stringer2
	
	elif "A" not in string and "B" not in string and "K" in string and "H" not in string:
		stringer3 = replace(string, "K", "|<")
		return stringer3
	
	elif "A" not in string and "B" not in string and "K" not in string and "H" in string:
		stringer4 = replace(string, "H", "|-|")
		return stringer4
	
	elif "A" in string and "B" in string and "K" not in string and "H" not in string:
		stringer1 = replace(string, "A", "@")
		stringer2 = replace(stringer1, "B", "|3")
		return stringer2
	
	elif "A" in string and "B" not in string and "K" in string and "H" not in string:
		stringer1 = replace(string, "A", "@")
		stringer3 = replace(stringer1, "K", "|<")
	
	elif "A" in string and "B" not in string and "K" not in string and "H" in string:
		stringer1 = replace(string, "A", "@")
		stringer4 = replace(stringer1, "H", "|-|")
		return stringer4
	
	elif "A" not in string and "B" in string and "K" in string and "H" not in string:
		stringer2 = replace(string, "B", "|3")
		stringer3 = replace(stringer2, "K", "|<")
		return stringer3
	
	elif "A" not in string and "B" in string and "K" not in string and "H" in string:
		stringer2 = replace(string, "B", "|3")
		stringer4 = replace(stringer2, "H", "|-|")
		return stringer4
	
	elif "A" not in string and "B" not in string and "K" in string and "H" in string:
		stringer3 = replace(string, "K", "|<")
		stringer4 = replace(stringer3, "H", "|-|")
		return stringer4
	
	elif "A" in string and "B" in string and "K" in string and "H" not in string:
		stringer1 = replace(string, "A", "@")
		stringer2 = replace(stringer1, "B", "|3")
		stringer3 = replace(stringer2, "K", "|<")
		return stringer3
	
	elif "A" in string and "B" not in string and "K" in string and "H" in string:
		stringer1 = replace(string, "A", "@")
		stringer3 = replace(stringer1, "K", "|<")
		stringer4 = replace(stringer3, "H", "|-|")
		return stringer4
	
	elif "A" not in string and "B" in string and "K" in string and "H" in string:
		stringer2 = replace(string, "B", "|3")
		stringer3 = replace(stringer2, "K", "|<")
		stringer4 = replace(stringer3, "H", "|-|")
		return stringer4
	
	elif "A" in string and "B" in string and "K" in string and "H" in string:
		stringer1 = replace(string, "A", "@")
		stringer2 = replace(stringer1, "B", "|3")
		stringer3 = replace(stringer2, "K", "|<")
		stringer4 = replace(stringer3, "H", "|-|")
		return stringer4
	
	
	
	
	


def main():
	string = input("Choose a string: ")
	puncs = "!@#$%^&*{}|:.,;'"
	string_with_no_punctuations = ""
	for character in string:
		if character not in puncs:
			string_with_no_punctuations += character
	
	
	lower_to_upper(string_with_no_punctuations)
	print(lower_to_upper(string_with_no_punctuations))
	phrase_to_acronym(lower_to_upper(string_with_no_punctuations))
	print(phrase_to_acronym(lower_to_upper(string_with_no_punctuations)))
	letter_to_homoglyph(phrase_to_acronym(lower_to_upper(string_with_no_punctuations)))
	print(letter_to_homoglyph(phrase_to_acronym(lower_to_upper(string_with_no_punctuations))))
	
	
	
main()




			


	
