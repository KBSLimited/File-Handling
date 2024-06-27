import os

def list_directory_contents(path):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(path)
        
        # Print each item in the contents list
        for item in contents:
            print(item)
            
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Prompt user for directory path
directory_path = input("Enter the directory path: ")

# Call the function to list directory contents
list_directory_contents(directory_path)