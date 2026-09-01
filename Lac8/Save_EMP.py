num_emps = int (input("How many employees do you want to record?"))
with open("employees.txt", "w") as emp_file:
    for count in range(1, num_emps + 1):
        print('Enter data for employee #', count, sep='')
        name = input("Enter employee name: ")
        id = input("Enter employee ID: ")
        dept = input("Enter employee department: ")
        emp_file.write(name + '\n')
        emp_file.write(id + '\n')
        emp_file.write(dept + '\n')
        print()

    print(f"Employee data for {num_emps} employees has been recorded in 'employees.txt'.")