# Winders Arias
# 5/8/2024

# Creating an empty list
lst = []

# Using a for loop to add the numbers 1 through 100 to the list
for i in range(1, 101):
    lst.append(i)

# Printing the list lst
print(lst)

# Creating an empty list named odd
odd = []

# Using a for loop to add the odd numbers 1 through 100 to the list odd
for i in range(1, 101, 2):
    odd.append(i)

# Printing the list odd
print(odd)

# Creating an empty list named even
even = []

# Using a for loop to add the even numbers 1 through 100 to the list even
for i in range(2, 101, 2):
    even.append(i)

# Printing the list even
print(even)

# Create a variable named "b" that points to the first list that you created
b = lst

# Create a variable named joined that joins the even and odd lists using an operator
joined = odd + even

# Output the variable joined
print(joined)

# Output the type of the variable joined
print(type(joined))

# Compare the list b to the list joined using positional comparison
print(joined == b)