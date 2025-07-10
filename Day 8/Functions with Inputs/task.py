def greet():
    print("Hello!")
    print("How are you doing today?")
    print("Have a great day")

greet()

# Functions that allows for inputs
name = input("Enter your name: ")
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How are you doing {name}?")
    print(f"Have a great day {name}!")

greet_with_name(name)

# Coding challenge
# Create a function called life_in_weeks() using maths and f-Strings that tells
# us how many weeks we have left, if we live until 90 years old.

def life_in_weeks(age):
    years_left = 90 - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(20)