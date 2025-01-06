#1
# Example using len() to find the length of a list
my_list = [10, 20, 30, 40, 50]
length_of_list = len(my_list)
print(f"The length of the list is: {length_of_list}")

#output
#The length of the list is: 5

#2
# Function to greet a person
def greet(name):
    print(f"Hello, {name}!")

# Example of calling the function
greet("John")

#output Hello, John!

#3
# Function to find the maximum value in a list of numbers
def find_maximum(numbers):
    max_value = numbers[0]  # Start with the first number as the maximum
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Example usage
numbers = [12, 45, 23, 67, 34]
max_number = find_maximum(numbers)
print(f"The maximum number is: {max_number}")

#output
#The maximum number is: 67

#4
# Global variable
name = "Global Name"

def test_variable_scope():
    # Local variable with the same name as the global variable
    name = "Local Name"
    print("Inside the function, name is:", name)

# Calling the function
test_variable_scope()

# Accessing the global variable outside the function
print("Outside the function, name is:", name)

#5
# Function to calculate the area of a rectangle with default width as 5
def calculate_area(length, width=5):
    area = length * width
    return area

# Calling the function with both length and width
area_with_width = calculate_area(10, 6)
print(f"The area with width 6 is: {area_with_width}")

# Calling the function with only the length, default width of 5 will be used
area_with_default_width = calculate_area(10)
print(f"The area with default width 5 is: {area_with_default_width}")


