#Write your code below this row 👇
print("Calculating the sum of all even numbers between 1 to 100")
sum = 0
for num in  range(0,101,2):
 sum+=num
print(f"The sum of all even numbers between 1 to 100 is {sum}")

#step in range is used here  rather than checking whether the number in the loop is even or odd
