with open('sales.txt', 'r') as sales_file:
    for line in sales_file:
       sales = float(line.strip())
    print(f"Sales: {sales:.2f}")

   
