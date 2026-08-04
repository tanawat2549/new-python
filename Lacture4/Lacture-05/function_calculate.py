def calculate_stats(numbers):
    tital_sm = sum(numbers)
    average = tital_sm / len(numbers)
    maximun = max(numbers)
    minimun = min(numbers)
    return tital_sm, average, maximun, minimun
numbers = [5 , 10 , 15 , 20 , 25]
total , avg, max_num, min_num = calculate_stats(numbers)
print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")