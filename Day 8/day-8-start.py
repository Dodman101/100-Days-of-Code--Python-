#Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code. 

# def greet():
#     print("Hello!")
#     print("Good morning!")
#     print("Hola!")

# greet()

# Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Dodman")

#Functions with more than 1 input (and are positional arguments the argument "Dodman" is not tied to the paramemter "name")
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is the weather like in {location}")

# greet_with("Dodman", "Kenya")

#Functions with Keyword Arguments
greet_with(name="Dodman", location="Kenya")