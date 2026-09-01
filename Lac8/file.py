def example_a_plus_mode():
    # Open a file in 'a+' mode (append and read)
    with open('example_a+.txt', 'a+') as file:
       file.seek(0)  # Move the cursor to the beginning of the file
       conteant = file.read()  # Read the existing content
       print("Current content of the file:")
    print(conteant)
    file.write('Appending a new line to the file.\n')  # Append new data
    file.seek(0)  # Move the cursor back to the beginning of the file
    updated_content = file.read()  # Read the updated content
    print("Updated content of the file:")
    print(updated_content)
    
    example_a_plus_mode()