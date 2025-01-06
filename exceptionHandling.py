# Exercise 1: Read a file and display its contents
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")

# Example usage
file_name = input("Enter the filename to read: ")
read_file(file_name)


# Exercise 2: Copy the contents of one file to another file
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()

        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Contents copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"Error: {source_file} not found.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")
copy_file(source_file, destination_file)


# Exercise 3: Read the content of a file and count the total number of words
def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")

# Example usage
file_name = input("Enter the filename to count words: ")
count_words_in_file(file_name)

# Exercise 4: Convert a string to an integer using try-except blocks
def convert_to_integer():
    user_input = input("Enter a string to convert to integer: ")
    try:
        result = int(user_input)
        print(f"Converted integer: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

# Example usage
convert_to_integer()


# Exercise 5: Raise an exception if any integers in the list are negative
def check_negative_integers():
    try:
        user_input = input("Enter a list of integers separated by spaces: ")
        numbers = list(map(int, user_input.split()))

        for num in numbers:
            if num < 0:
                raise ValueError("Negative number detected!")

        print("All numbers are non-negative.")
    except ValueError as e:
        print(f"Error: {e}")


# Example usage
check_negative_integers()


# Exercise 6: Compute the average of integers with try-except and finally clause
def compute_average():
    try:
        user_input = input("Enter a list of integers separated by spaces: ")
        numbers = list(map(int, user_input.split()))

        if len(numbers) == 0:
            raise ValueError("The list is empty.")

        average = sum(numbers) / len(numbers)
        print(f"The average is: {average}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Program finished running.")


# Example usage
compute_average()


# Exercise 7: Write a string to a file with try-except blocks
def write_to_file():
    file_name = input("Enter the filename to write to: ")
    content = input("Enter the string to write to the file: ")

    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Content written to {file_name} successfully!")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Welcome! The content was written without any issues.")


# Example usage
write_to_file()


