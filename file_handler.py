# file_handler.py

def modify_content(content):
    """
    Modify the file content.
    For example, convert text to uppercase.
    You can change this logic later if needed.
    """
    return content.upper()


def main():
    try:
        # Ask user for a file name
        filename = input("Enter the filename to read: ")

        # Try opening the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create a new filename for the output
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
