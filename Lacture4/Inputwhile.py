import random

print("what is my magig number ( 1 to 100)?")
my_number = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess:
    msg = str(ntries) + ">>"
    if (ntries ==6):
        msg = "last chance>>"
    yourguess = int(input(msg))
    if yourguess == my_number:
        print("--> too high")
    elif yourguess < my_number:
        print("--> too low")
    ntries += 1
if yourguess == my_number:
   print("Yes! it's" my_number)
else :
  print("Sorry! my number is", my_number)
