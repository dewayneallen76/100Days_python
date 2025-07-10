# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jack Bauer")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"How is it in {location}?")

greet_with("Dewayne", "Riceville")

# Keyword arguments
greet_with(name="Kristy", location="Cleveland")

