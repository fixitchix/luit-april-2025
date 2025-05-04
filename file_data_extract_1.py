import os
import datetime # We need this to format date and time to make it readable
from tabulate import tabulate

# Get our cwd
cwd = os.getcwd()

# Get a list of files in our cwd
files = os.listdir(cwd)

# Create empty list to store our cwd file info.
file_dictionary_list = []

# Iterate each file in our cwd
for file_name in files:

    # Get the full path of the file
    full_path = os.path.join(cwd, file_name)
    
    # Check if it's a file and NOT a directory
    if os.path.isfile(full_path):
        
        # Get the file size
        file_size = os.path.getsize(full_path)
       
        # Get file creation info (timestamp)
        file_creation = os.path.getctime(full_path)
        
        # Convert the timestamp to a human-readable format
        file_creation = datetime.datetime.fromtimestamp(file_creation).strftime('%Y-%m-%d %H:%M:%S')
  
        # Create dictionary with file information
        file_info = {
            "file_name": file_name,
            "file_path": full_path,
            "file_size": file_size,
            "file_creation": file_creation
        }

        # Add file info. to the dictionary list
        file_dictionary_list.append(file_info)

# Print the file information as a table
# Extract keys for headers and list of values for rows
headers = file_dictionary_list[0].keys() if file_dictionary_list else []
rows = [list(file.values()) for file in file_dictionary_list]

# Print the formatted table using tabulate
print(tabulate(rows, headers=headers, tablefmt="pretty"))




