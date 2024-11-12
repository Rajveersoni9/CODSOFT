import random
import string

def generate_password(num_letters, num_numbers, num_symbols):
#Generate a random password using for loops
    password_list = []

    for _ in range(num_letters):
        password_list.append(random.choice(string.ascii_letters))
    for _ in range(num_numbers):
        password_list.append(random.choice(string.digits))
    for _ in range(num_symbols):
        password_list.append(random.choice(string.punctuation))

    random.shuffle(password_list)
    return ''.join(password_list)

# Get user input for the number of letters, numbers, and symbols
try:
    num_letters = int(input("Enter the number of letters: "))
    num_numbers = int(input("Enter the number of numbers: "))
    num_symbols = int(input("Enter the number of symbols: "))

# Generate and display the password
    generated_password = generate_password(num_letters, num_numbers, num_symbols)
    print("Generated password:",generated_password)
except ValueError:
    print("Please enter valid numbers.")
    
