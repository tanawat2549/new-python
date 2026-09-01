with open('sales.txt', 'r') as sales_file:
    line = sales_file.readline()
    while line: 
        sales = float(line.strip())
        print(f"Sales: {sales:.2f}")
        line = sales_file.readline()