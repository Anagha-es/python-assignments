# MonthNames.py
month_dict = {
    1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
}

month = int(input("Enter the month: "))
if 1 <= month <= 12:
    print(f"Month {month} is {month_dict[month]}")
else:
    print("Invalid month.")


#2
# Cinema Ticket Price
age = int(input("Enter your age: "))
if age < 16:
    price = 6 / 2  # Half price for people under 16
elif age >= 60:
    price = 6 / 3  # One-third price for people 60 or older
else:
    price = 6  # Full price
print(f"Your ticket costs £{price:.2f}")


#3
# BodyMassIndex.py
weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are in the 'underweight' range.")
elif 18.5 <= bmi <= 24.9:
    print("You are in the 'normal' range.")
elif 25 <= bmi <= 29.9:
    print("You are in the 'overweight' range.")
else:
    print("You are in the 'obese' range.")


#4
# Greatest of Three Numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")


#5
# Factorial of a Number Using Loops
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")

#6
# Reverse a Number Using While Loop
num = int(input("Enter a number: "))
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"The reversed number is: {reversed_num}")

#7
# Finding Multiples of a Number Using Loop
num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))
print(f"Multiples of {num} up to {limit}:")
for i in range(1, limit + 1):
    if i % num == 0:
        print(i)


#8
# Print and Break on 'done'
while True:
    user_input = input()
    print(user_input)
    if user_input.lower() == 'done':
        break


#9
# FizzBuzz
for num in range(1, 11):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


#10
# Print Pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
