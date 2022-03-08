import random

# defining the function generate_password that takes in one argument, length
def generate_password(upper_case_letters, lower_case_letters, numbers, special_characters, length):
  # local variables - can ONLY be accessed/used within the scope of this function, generate_password
  #initalizing/setting the list and variable to an empty list and empty string, respectively
  new_password = []
  password_string = ''

  # while the length of the list, new_password, is less than the password_length specified below, do all this in the while loop
  while len(new_password) < length:
    # if length of the new_password list is less than length (which is the password_length), then get random lowercase letter and append it to the list, new_password
    # else break out of the while loop
    if len(new_password) < length:
      new_password.append(random.choice(lower_case_letters))
    else:
      break
    # if length of the new_password list is less than length (which is the password_length), then get random uppercase letter and append it to the list, new_password
    # else break out of the while loop
    if len(new_password) < length:
      new_password.append(random.choice(upper_case_letters))
    else:
      break
    # if length of the new_password list is less than length (which is the password_length), then get random number and append it to the list, new_password
    # else break out of the while loop
    if len(new_password) < length:
      new_password.append(random.choice(numbers))
    else:
      break
    # if length of the new_password list is less than length (which is the password_length), then get random special_character and append it to the list, new_password
    # else break out of the while loop
    if len(new_password) < length:
      new_password.append(random.choice(special_characters))
    else:
      break

  # DEBUGGING - used to see what the inital generated list is
  print('DEBUG : new_password:', new_password)
  # shuffle the new_password list to make it more random
  random.shuffle(new_password)
  # DEBUGGING - used to verify what the first item in the list is to determine if we need to go into the while loop below (line 94) or can skip it
  print('DEBUG : initial shuffle:', new_password)

  # after shuffling, if the first item in the list is either a special character or a number, shuffle again
  # shuffle until the first character is NOT a special charater or a number
  while (new_password[0] in special_characters) or (new_password[0] in numbers):
    random.shuffle(new_password)
    # DEBUGGING - used to verify the list does not have a special character or number as its first item before making it into a string
    # this prints every time list is shuffled within this while loop
    print('DEBUG : shuffled password:', new_password)
  
  # add all the items into a list and make it into a string
  # this says, "as long as there is an 'item' in the list new_password, add the 'item' to the password_string
  # password_string starts as an empty string. each time it iterates through the list, new_password, it takes the item (first to last)
  # and adds it to the string, password_string
  for item in new_password:
    password_string+=item

  #return the password_string so it can be used outside of this function
  return password_string