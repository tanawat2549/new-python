num_days = int(input("For how many days do you want to record sales? "))
with open("sales.txt", "w") as sales_file:
    for count in range(1, num_days + 1):
        sales = float(input(f"Enter sales for day {count}: "))
        sales_file.write(f"{sales}\n")

    print(f"Sales data for {num_days} days has been recorded in 'sales.txt'.")
    