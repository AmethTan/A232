# Create a dictionary of student information
student = {
    "name": "Bernard",
    "age": int(22),
    "major": "Decision Science",
    "grades": {
        "math": 98,
        "english": 91,
        "programming": 95
    }
}

# Access dictionary values by keys
student_name = student["name"]
student_age = student["age"]

# Modify dictionary values
student["age"] = 24
student["grades"]["math"] = 100

# Add a new key-value pair
student["gender"] = "Male"

# Check if a key exists in the dictionary
has_major = "major" in student
has_height = "weight" in student

# Get the list of keys and values
keys = student.keys()
values = student.values()
print(keys)
print(values)
print()

# Iterate through the dictionary
print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Remove a key-value pair
del student["major"]

# Print the updated dictionary
print("\nStudent Information after removing 'major':")
for key, value in student.items():
    print(f"{key}: {value}")

# Modified for learning purpose by Tan Yu Xian
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my
