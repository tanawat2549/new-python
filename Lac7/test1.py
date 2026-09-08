attendance_week = [
    ["Alice", "Bob", "Charlie" , "David"],
    ["Alice" , "Bob", "David"],
    ["Alice", "Bob", "David"],
    ["Alice", "Bob", "David", "Eve"],
    ["Bob", "David", "Charlie"],
]


attendance_set = [set(day) for day in attendance_week]
print (attendance_set)

present_all_days = set.intersection(*attendance_set)
print("Students present every day:", present_all_days)

all_students = set.union(*attendance_set)
absent_at_least_one_day = all_students - present_all_days
print("Absent at least one day:", absent_at_least_one_day)

first_day_present = attendance_set[0]
last_day_present = attendance_set[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("Present on first day but absent on last day:", first_day_but_not_last)

unique_students_count = len(all_students)
print("Total unique students:", unique_students_count)

