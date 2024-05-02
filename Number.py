# Get user input for integer and floating-point numbers
x = float(input("Please a number (x): "))
y = float(input("Please another number (y): "))
z = int(input("Please an integer (z): "))

# Perform arithmetic operations
sum_xy = x + y
difference_xy = x - y
product_xz = x * z
quotient_xz = x / z
modulus_xz = x % z
exponentiation_xz = x ** z

# Print the results
print("x + y =", sum_xy)
print("x - y =", difference_xy)
print("x * z =", product_xz)
print("x / z =", quotient_xz)
print("x % z =", modulus_xz)
print("x ** z =", exponentiation_xz)

# Use built-in functions for numerical operations
absolute_z = abs(z)
rounded_y = round(y)
max_value = max(x, y, z)
min_value = min(x, y, z)

print("Absolute value of z:", absolute_z)
print("Rounded value of y:", rounded_y)
print("Max value:", max_value)
print("Min value:", min_value)

# Import the math module for more advanced math operations
import math

square_root_x = math.sqrt(x)
logarithm_base_10_x = math.log10(x)
factorial_z = math.factorial(abs(z))

print("Square root of x:", square_root_x)
print("Logarithm base 10 of x:", logarithm_base_10_x)
print(f"Factorial of |z| ({abs(z)}):", factorial_z)

# Modified for learning purpose by Tan Yu Xian
# Created by Dr Aamir Adeeb
# Contact for more info at aamir@uum.edu.my