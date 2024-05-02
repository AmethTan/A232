# Define a string variable
greet = "Hello, World! My name is Tan Yu Xian"

# Print the string
print(greet)

# Access individual characters in the string
twelfth_character = greet[12]
print("The 12th character is:", twelfth_character)

# Find the length of the string
lengthOfGreet = len(greet)
print("The length of the string is:", lengthOfGreet)



#
# Get user input for the name
userName = input("Please enter your name here.  ")
#
#



# Concatenate (combine) two strings
greetUser = "Good day, " + userName + "!"
print(greetUser)

# Use string methods
uppercaseMessage = greetUser.upper()
print("Uppercase message:", uppercaseMessage)

# Check if a substring is in the string
contains = "world" in greetUser
print("Does the message contain 'world'? ", contains)

# Replace part of the string
newMessage = greetUser.replace("world", "World")
print("Updated message:", newMessage)

# Modified for learning purpose by Tan Yu Xian
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my