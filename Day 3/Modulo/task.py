# The modulo operator gives you the remainder of a division

print(10 % 3)

# Odd or even
# Check if the number inputted is odd or even
# Convert to integer
# Even number % 2 == 0
print("Check to see if your number is odd or even")
entered_number = input("Enter a number: ")

if int(entered_number) % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
