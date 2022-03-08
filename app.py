import sys
sys.path.insert(0, 'methods')

from generate_password import generate_password


lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# combining all the letters together into one list
# all_letters = lower_case_letters + upper_case_letters

# global variable
# initializing/setting the variable password to be an empty string
password = ''
  
# beginning of the actual program
password_length = int(input('How long should the password be? (Mininum length of 4) '))

# only goes into this while loop if password_length entered by user is less than 4
while password_length < 4:
  print("Password must be at least 4. ")
  password_length = int(input('How long should the password be? '))

# assign the returned value from the function generate_password, password_string, to the variable password
password = generate_password(upper_case_letters, lower_case_letters, numbers, special_characters, password_length)

# print the password to the user
print('Your password is: ', password)

# DEBUGGING - used to verify password is of correct length
print(f'DEBUG : password length: {password_length}')