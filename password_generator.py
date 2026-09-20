import random

# Lists containing the possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

# Ask the user how many of each type of character they want
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_number = int(input("How many numbers would you like in your password?\n"))

# Create an empty list to store the password characters
password_list= []

# Pick a random letter and add it to the password list
# Repeat this based on how many letters the user requested
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

# Pick random symbols and add them to the password list
# Repeat this based on how many symbols the user requested
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

# Pick random numbers and add them to the password list
# Repeat this based on how many numbers the user requested
for char in range(0, nr_number):
    password_list.append(random.choice(numbers))

# Randomly rearrange all the characters in the list
random.shuffle(password_list)


# Create an empty string for the final password
password = ""

# Go through each character in the list
# Add each character to the password string
for char in password_list:
    password += char
print(f"Your password is:{password}")



