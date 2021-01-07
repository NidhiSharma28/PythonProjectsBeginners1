# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
str2 = name1 + name2
combined_str = str2.lower()
print(combined_str)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
T = combined_str.count("t")
R = combined_str.count("r")
U = combined_str.count("u")
E = combined_str.count("e")
L = combined_str.count("l")
O = combined_str.count("o")
V = combined_str.count("v")
E = combined_str.count("e")
true = T + R + U + E
love = L + O +V + E
sum = int(str(true) + str(love))
print(sum)
if sum < 10 or sum > 90:
  print(f"Your score is **{sum}**, you go together like coke and mentos.")
elif sum >=40 or sum<=50:
  print(f"Your score is **{sum}**, you are alright together.")
else:
  print(f"Your score is **{sum}**.")

