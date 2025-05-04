import os
from tabulate import tabulate

# Get the current working directory
cwd = os.getcwd()

# Get a list of files in the working directory
files = os.listdir(cwd)

# Create an empty list to store file information
dictionary_list = []

# Iterate over each file in the directory
for file_name in files:
    # Get the full path of the file
    file_path = os.path.join(cwd, file_name)
    
    # Get the file size in bytes
    file_size = os.path.getsize(file_path)
    
    # Get the file creation time
    creation_time = os.path.getctime(file_path)

    # Defining rows
    rows = [list(file.values()) for file in dictionary_list]
   
    # Create a dictionary with file information
    file_info = {
        'file_name': file_name,
        'file_path': file_path,
        'file_size': file_size,
        'creation_time': creation_time
    }
    
    # Add the file information to the list
    dictionary_list.append(file_info)

# Defining rows
rows = [list(file.values()) for file in dictionary_list]

# Check if file_dictionary_list is not empty
if dictionary_list:
    headers = dictionary_list[0].keys()  # Get the keys (headers) from the first dictionary
else:
    headers = []  # If file_dictionary_list is empty, use an empty list for headers

# Print the formatted table using tabulate
print(tabulate(rows, headers=headers, tablefmt="pretty"))






