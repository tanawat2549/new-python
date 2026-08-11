fruits_With_duplicates = ["apple", "banana",  "apple", "cherry", "apple","kivi"]
while "apple" in fruits_With_duplicates:
    fruits_With_duplicates.remove("apple")
print(f"Fruits after removing duplicates: {fruits_With_duplicates}")