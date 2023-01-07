# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passcode = ""
passcode_list = []
for char in range(1, nr_letters + 1):
    rand_char = random.choice(letters)

    passcode_list += rand_char

for symbol in range(1, nr_symbols + 1):
    rand_symbol = random.choice(symbols)
    passcode_list += rand_symbol

for num in range(1, nr_numbers + 1):
    rand_num = random.choice(numbers)
    passcode_list += rand_num
# print(passcode_list)
random.shuffle(passcode_list)
# print(passcode_list)
final_password = ""
for passcode in passcode_list:
    final_password += passcode

print("Your Password is:",final_password)

