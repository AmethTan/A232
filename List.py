# Create a list of numbers
numbers = [5, 4, 3, 2, 1]

# Print the list
print("First list:", numbers)

# Access elements by index
last_element = numbers[-1]
print("The last element is:", last_element)


# Slice the list to get a subset
subset = numbers[1:3]
print("Subset of the list:", subset)

# Modify an element in the list
numbers[0] = 10
print("Modified list:", numbers)



# Append an element to the end of the list
numbers.append(8)
print("List after appending 8:", numbers)

# Remove an element by value
numbers.remove(2)
print("List after removing 2:", numbers)


# Find the index of an element
index_of_3 = numbers.index(3)
print("Index of 3:", index_of_3)

# Check if an element is in the list
contains_6 = 6 in numbers
print("Does the list contain 6?", contains_6)


# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)

 
# Create a list of strings
veges = ["cabbage", "carrot", "spinach", "tomato"]

print(veges[2])

# Modified by Tan Yu Xian for learning purpose
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my
