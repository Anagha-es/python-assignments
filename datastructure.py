
# Create a list of 5 random numbers and print the list
random_numbers = [10, 23, 45, 67, 89]
print(random_numbers)
# Insert 3 new values to the list and print the updated list
random_numbers.extend([12, 34, 56])  # Add 3 new numbers
print(random_numbers)
# Use a for loop to print each element in the list
for number in random_numbers:
    print(number)


# Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively
person = {
    'name': 'John',
    'age': 25,
    'address': 'New York'
}
print(person)
# Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'
person['phone'] = '1234567890'
print(person)


# Create a set with values 1, 2, 3, 4, and 5
my_set = {1, 2, 3, 4, 5}
print(my_set)
# Add the value 6 to the set created in Q1
my_set.add(6)
print(my_set)
# Remove the value 3 from the set created in Q1
my_set.remove(3)  # Remove the element 3 from the set
print(my_set)


# Create a tuple with values 1, 2, 3, and 4
my_tuple = (1, 2, 3, 4)
print(my_tuple)
# Print the length of the tuple created in Q1
tuple_length = len(my_tuple)
print(f"The length of the tuple is: {tuple_length}")
