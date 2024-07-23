'''
    Handling Files in Python

    In Python, file handling is an essential skill that allows you to read from and write to files.
    This is useful for tasks such as saving data, loading configuration settings, or processing logs.
    Function open() -> built in Fn
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
 
file_path = 'sample.txt'
student_data = {
    "Name": 'Abdulhameed',
    "Student_id": 2389990,
    "Course": "Python Programming",
    "Course_Code": "CSC201",
    "Grade": "A"
}
student_data_2 = {
    "Name": 'Yunusa',
    "Student_id": 2389990,
    "Course": "Python Programming",
    "Course_Code": "CSC201",
    "Grade": "A+"
}

def writeFile(file_path, student_data):
    '''
        description: saves data to a txt file
        args: file_path(str), data(dictionary)
        return : None 
    '''
    while True:
        try:
            with open(file_path, "x") as f:
                f.write(str(student_data))
            print("Write Operation Successful")
            break
        except FileExistsError as e:
            with open(file_path, "a") as f:
                f.write(str(student_data))
            print("Data appended to the end of file", e)
            break
        
writeFile(file_path, student_data)     
writeFile(file_path, student_data_2)

'''
    Performing a read operation 
'''
def readFile(file_path):
    with open(file_path, encoding="utf-8") as f:
        read_data = f.readline()
        print(read_data)
readFile(file_path)