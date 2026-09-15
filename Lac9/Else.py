try:
    value = int (input("Enter a number:"))
    reesult = 10 / value
except ZeroDivisionError:
     print("Cannot divide by zero!")
else:
     print (f"THe result is {reesult}")

print("End of program")