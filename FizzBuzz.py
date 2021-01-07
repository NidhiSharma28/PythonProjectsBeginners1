#Your program should print each number from 1 to 100 in turn.
#When the number is divisible by 3 then instead of printing the number it should print "Fizz".

print("**Welcome to FizzBuzz game!!!***")
for num in range(1,101):
  if(num%3==0):
    if(num%5==0):
      print("FizzBuzz")
    else:
      print("Fizz")
  elif(num%5==0):
    if(num%3==0):
      print("fizzBuzz")
    else:
      print("Buzz")    
  else:
    print(num)
print("Game over.Thanks!")
