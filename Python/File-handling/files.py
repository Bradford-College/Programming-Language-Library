'''
    Handling Files in Python

    In Python, file handling is an essential skill that allows you to read from and write to files.
    This is useful for tasks such as saving data, loading configuration settings, or processing logs.

    Basic file operations include:
    - Opening a file
    - Reading from a file
    - Writing to a file
    - Closing a file

    Python provides built-in functions and the 'with' statement to make file handling easier and safer.

    File Modes:
    - 'r': Open a file for reading (default mode).
    - 'w': Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
    - 'a': Open a file for appending. Data is added to the end of the file if it exists.
    - 'b': Open a file in binary mode.
    - 'x': create blank file 
    - 't': Open a file in text mode (default mode).
    - '+': Open a file for updating (reading and writing).
'''

# Define the file path directly
#file_path = '/Users/abdulhameed/Documents/Programming Language Library /Python/File-handling/sample.txt'
file_path = 'sample.txt'
# Sample data to be written to the file
student_data = {
    'Name': 'Abdulhameed',
    'ID_Num': 100345,
    'Class': 'Object Oriented Programming',
    'Level': 'Year 5'
}

# Function to write student bio data to a file
def studentBio(file_path, student_data_):
    try:
        # Try to open the file in 'x' mode to create it if it doesn't exist
        with open(file_path, 'x') as f:
            # Convert dictionary to string and write to the file
            f.write(str(student_data))
    except FileExistsError:
        try:
            # If the file already exists, open it in write mode
            with open(file_path, 'w') as f:
                # Convert dictionary to string and write to the file
                f.write(str(student_data))
        except TypeError as e:
            # Handle the case where the write operation failed
            print("Write Error:", e)
    except TypeError as e:
        # Handle the case where the write operation failed
        print("Write Error:", e)
        

# Call the function to write the student data to the file
studentBio(file_path, student_data)