import random
letters = int(input("How many letters?"))
numbers = int(input("How many numbers?"))
symbols = int(input("How many symbols?"))
letters_str = ""
numbers_str = ""
symbols_str = ""
passwordlist = []
while len(letters_str) < letters:
  res = input("Enter the letter ")
  if res.isalpha():
    letters_str = letters_str + res
    continue
  else:
    print("Wrong input! Try again")
while len(numbers_str) < numbers:
  res = input("Enter the number ")
  if res.isdigit():
    numbers_str = numbers_str + res
    continue
  else:
    print("Wrong input! Try again")  
while len(symbols_str) < symbols:
  res = input("Enter the symbol ")
  if res.isdigit() or res.isalpha():
    print("Wrong input! Try again")  
  else:
    symbols_str = symbols_str + res
    continue    
print("your password is :")
password = numbers_str + letters_str + symbols_str
for item in range(len(password)):
  passwordlist.append(password[item])
count = len(passwordlist)
new_password =""
for i in range(count):
  ch = random.choice(passwordlist)
  new_password = new_password + ch
  passwordlist.remove(ch)
print(new_password)
