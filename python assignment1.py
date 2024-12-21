1
print("Bob")
print("ST1001")
print("bob@gmail.com")
2
print("Bob\nST1001\nbob@gmail.com")
3
num1 = 14
num2 = 7

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {num1 / num2}")
4
for i in range(1, 6):
    print(i)
5
print("\"SDK\" stands for \"Software Development Kit\", whereas\n\"IDE\" stands for \"Integrated Development Environment\".")
6
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")  # ASCII for 65 is 'A'
print("\x65")  # Hex representation of 65 is 'e'
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

7
num = 23
textnum = "57"
decimal = 98.3

print(type(num))        # <class 'int'>
print(type(textnum))    # <class 'str'>
print(type(decimal))    # <class 'float'>

# Sum after converting 'textnum' to integer
sum_result = num + int(textnum) + decimal
print(f"Sum of variables: {sum_result}")
print(type(sum_result))  # Check the data type of the sum


8
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

# Calculate total minutes in a year
total_minutes_in_year = days_in_year * hours_in_day * minutes_in_hour
print(f"There are {total_minutes_in_year} minutes in a year.")

9
name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")

10
# PoundsToDollars.py

pounds = float(input("Please enter amount in pounds: "))
dollars = pounds * 1.25  # Assuming 1 pound = 1.25 dollars (example exchange rate)

print(f"£ {pounds} are $ {dollars}")




