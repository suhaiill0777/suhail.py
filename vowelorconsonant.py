def check_character(char):
   # Define vowels
   vowels = "aeiouAEIOU"
   # Check if the character is a vowel
   if char in vowels:
       print(f"The character '{char}' is a Vowel.")
   elif char.isalpha(): # Check if it's an alphabet but not a vowel
       print(f"The character '{char}' is a Consonant.")
   else:
       print(f"The character '{char}' is not an alphabet.")
# Input from the user
character = input("Enter a single character: ")
# Validate input length
if len(character) == 1:
   check_character(character)
else:
   print("Please enter only one character.")