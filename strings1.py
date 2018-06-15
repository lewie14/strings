my_name = "Mark"
first_initial = my_name[0]

first_name = "Rodrigo"
last_name = "Villanueva"

#make username by taking first 5 letters of last name
new_account = last_name[:5]
#make password from the 3rd to 6th letter of last name
temp_password =  last_name[2:6] 

first_name = "Julie"
last_name = "Blevins"

#username generator takes first 3 letters of first and last names
def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name
  
new_account = account_generator(first_name, last_name)

print(new_account)

print("----------------------------")

first_name = "Reiko"
last_name = "Matsuki"
#password generator takes last 3 letters of first and last names
def password_generator(first_name, last_name):
  password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return password
  
temp_password = password_generator(first_name, last_name)
print(temp_password)

print("----------------------------")
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]

final_word = company_motto[-4:]

print(second_to_last)
print(final_word)

print("----------------------------")
first_name = "Bob"
last_name = "Daily"

#Change Bob to Rob


fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)

print("----------------------------")

#escape character Backslash means ignore the next character in this case
password = "theycallme\"crazy\"91"
print(password)
print("----------------------------")
def get_length(string):
  count = 0
  for letter in string:
    count += 1
  return count
  
print("----------------------------")

# see if letter is in the word

def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False
  
print(letter_check("strawberry", "a"))

print("----------------------------")

# is little string in big string
def contains(big_string, little_string):
  if little_string in big_string:
    return True
  return False
  
print(contains("watermelon", "melon"))

print("----------------------------")


def contains(big_string, little_string):
  return little_string in big_string

#FInd common letters in string 1 and string 2
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(common_letters("banana", "cream"))


print("----------------------------")

#Make username from first 3 and first 4 of first and last names
def username_generator(first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    username = first_name + last_name
  else:
    username = first_name[:3] + last_name[:4]
  return username
  
#make password from username and shift all letters one to the right
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
    
print(username_generator("Mark", "Lewis"))
print(password_generator("Mark"))
