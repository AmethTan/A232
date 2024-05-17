# Create a tuple
veges = ("cabbage", "spinach", "tomato", "potato")

( "a" , 1 , 2.3 , "b"    )


# Access elements by index
third_vege = veges[2]
fourth_vege = veges[3]

# Iterate through the tuple
print("Veges:")
for vege in veges:
    print(vege)

# Check if an element is in the tuple
contains_cabbage = "cabbage" in veges

# Find the length of the tuple
num_veges = len(veges)

# Concatenate two tuples
more_veges = ("carrot", "beet")
all_veges = veges + more_veges

# Nested tuple
nested_tuple = ("small", ("large", "extra large"))

# Print the results
print("Third vege:", third_vege)
print("Fourth vege:", fourth_vege)
print("Does it contain 'cabbage'? ", contains_cabbage)
print("Number of veges:", num_veges)
print("All veges:", all_veges)
print("Nested tuple:", nested_tuple)

# Modified by Tan Yu Xian for learning purpose
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my
