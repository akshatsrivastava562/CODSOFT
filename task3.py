import random
import string

print("Welcome to the Password Generator")

length_input = input("How long should the password be? ")
length = int(length_input)

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_characters = lowercase + uppercase + digits + symbols

password_list = []

for i in range(length):
    char = random.choice(all_characters)
    password_list.append(char)

final_password = ""
for c in password_list:
    final_password += c

print("Your generated password is:")
print(final_password)