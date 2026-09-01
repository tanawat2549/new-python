with open("employees.txt", "r") as emp_file:
    line = emp_file.readline()
    while line != '':
        emp_name = line.strip()
        emp_id = emp_file.readline().strip()
        dept = emp_file.readline().strip()
        print(f"name: {emp_name}")
        print(f"ID: {emp_id}")
        print(f"Department: {dept}")
        line = emp_file.readline()