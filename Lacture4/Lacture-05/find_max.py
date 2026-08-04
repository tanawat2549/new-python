def find_max(*args):
    if not args:
        return None
    max_value = args[0]
    for number in args:
        if number > max_value:
            max_value = number
    return max_value
result1 = find_max(1, 2, 3, 4, 5)
result2 = find_max()
print(f"The maximum value is: {result1}")
print(f"The maximum value is: {result2}")