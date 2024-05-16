# Create a tuple
vege = ("spinach", "", "cherry", "date")

( "a" , 1 , 2.3 , "b"    )


# Access elements by index
first_vege = veges[0]
second_vege = veges[1]

# Iterate through the tuple
print("Veges:")
for vege in veges:
    print(vege)

# Check if an element is in the tuple
contains_cherry = "cherry" in veges

# Find the length of the tuple
num_veges = len(veges)

# Concatenate two tuples
more_veges = ("grape", "kiwi")
all_veges = veges + more_veges

# Nested tuple
nested_tuple = ("red", ("green", "blue"))

# Print the results
print("First vege:", first_vege)
print("Second vege:", second_vege)
print("Does it contain 'cherry'? ", contains_cherry)
print("Number of veges:", num_veges)
print("All veges:", all_veges)
print("Nested tuple:", nested_tuple)

# Modified by Tan Yu Xian for learning purpose
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my
