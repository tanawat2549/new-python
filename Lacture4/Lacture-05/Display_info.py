def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Tanawat", age=20, city="Bangkok")