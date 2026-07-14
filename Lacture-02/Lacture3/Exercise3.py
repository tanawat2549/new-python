hours = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly rate: "))

if hours <= 40:
    pay = hours * rate
else:
    overtime_hours = hours - 40
    pay = (40 * rate) + (overtime_hours * rate * 1.5)

print(f"The total pay is: ${pay:.2f}")