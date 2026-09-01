def example_w_plus_mode():
    # Open a file in 'w+' mode (write and read)
    with open('example_w+.txt', 'w+') as file:
        # Write some data to the file
        file.write('Hello, World!\n')
        file.write('This is an example of w+ mode.\n')
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Read the data back from the file
        content = file.read()
       
        print(content)
    example_w_plus_mode()