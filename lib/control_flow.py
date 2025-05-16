#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    username = username.lower()
    if username == "admin" and password == "12345":
        return "Access granted"
    elif username == "admin" or password == "12345":
        return "Access denied"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    # your code here
    if temperature <= 33:
        return "It's brisk out there!"
    elif temperature == 55:
        return "It's a little chilly out there!"
    elif temperature == 75:
        return "It's perfect out there!"
    elif temperature == 99:
        return "It's too dang hot out there!"
    else:
        return "That's not a temperature!"
    pass

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Division by zero is not allowed")
            return None
    else:
        print("Invalid operation!")
        return None
    pass
