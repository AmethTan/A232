#Sets are unordered collections of unique elements in Python. 
#They are often used when you need to work with a collection of 
#items where duplicates are not allowed, 
#or when you need to perform set operations like union and intersection.

# Create a set
veges = {"cabbage", "spinach", "tomato", "potato"}

# Add an element to the set
veges.add("carrot")

# Remove an element from the set
veges.remove("cabbage")

# Check if an element is in the set
contains_tomato = "tomato" in veges
contains_aragula = "aragula" in veges

# Iterate through the set
print("Veges:")
for vege in veges:
    print(vege)

# Create another set
ground_veges = {"carrot", "turnip", "radish","potato"}

# Perform set operations
union_veges_ground = veges.union(ground_veges)
intersection_veges_ground = veges.intersection(ground_veges)
difference_veges_ground = veges.difference(ground_veges)

# Print the results
print("Contains 'tomato'? ", contains_tomato)
print("Contains 'aragula'? ", contains_aragula)
print("Union of veges and ground veges:", union_veges_ground)
print("Intersection of veges and ground veges:", intersection_veges_ground)
print("Difference between veges and ground veges:", difference_veges_ground)

# Modified by Tan Yu Xian for learning purpose
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my
