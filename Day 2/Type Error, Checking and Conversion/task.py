print(len("12345"))

# Use type() to find the data type if you are unsure
print(type("Hello")) # <class 'str'>
print(type(12345))   # <class 'int'>
print(type(123.45))  # <class 'float'>
print(type(True))    # <class 'bool'>

# Type conversion
print("123" + "456")
# Since the data type above is a string the + will concatenate the strings
# By converting the strings to integers, it will treat them as integers and + will add the integers
print(int("123") + int("456"))

# Exercise: Make the below line of code run without errors
#print("Number of letters in your name: " + len(input("Enter your name")))

# Solution
number_of_letters = input("Enter your name") # str
length_of_name = len(number_of_letters) # int
print("Number or letters in your name: " + str(length_of_name)) # type conversion of int to str