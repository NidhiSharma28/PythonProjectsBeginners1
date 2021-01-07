#Password Generator Project
import random
import string
letters = list(string.ascii_letters)
numbers = list(range(0,9)) 
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = input("How many letters would you like in your password?\n")
nr_symbols = input(f"How many symbols would you like?\n")
nr_numbers = input(f"How many numbers would you like?\n")
while not nr_letters.isnumeric() or not nr_symbols.isnumeric() or not nr_numbers.isnumeric(): 
 print("Not all the values are numbers, retry.")
 nr_letters = input("How many letters would you like in your password?\n")
 nr_symbols = input(f"How many symbols would you like?\n")
 nr_numbers = input(f"How many numbers would you like?\n")
 
nr_letters = int(nr_letters) 
nr_symbols = int(nr_symbols)
nr_numbers = int(nr_numbers)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pwd_letters = ""
pwd_sym =""
pwd_num = ""
for a in range(1,nr_letters+1):
 pwd_letters = pwd_letters + random.choice(letters)
for a in range(1,nr_numbers+1):
 pwd_num = pwd_num + random.choice(numbers)
for a in range(1,nr_symbols+1):
 pwd_sym = pwd_sym + random.choice(symbols)
print("Congratulations, your password is successfully created")
print(f"Easy one : {pwd_letters+pwd_num+pwd_sym}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = pwd_letters+pwd_num+pwd_sym
count = len(password)
pass_list = []
for i in range(0,count):
 pass_list.append(password[i]);
hard_pwd=""
count1 = len(pass_list)
for i in range(count1):
  str = random.choice(pass_list)
  hard_pwd = hard_pwd + str
  pass_list.remove(str)
print(f"Hard one : {hard_pwd} ")
