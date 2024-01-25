# Aufgabe 1:
# Create a variable named CARNAME and assign the value VOLVO to it:
carname = "Volvo"
print(carname)

# Aufgabe 2:
# Create a variable named X and assign the value 50 to it:
x = 50
print(x)

# Aufgabe 3:
# Display the sum of 5 + 10, using two variables: x and y.
x = 5
y = 10
print(x+y)

# Aufgabe 4:
# Create a variable called z, assign x + y to it, and display the result.
x= 5
y= 10
z = x+y
print(z)

# Aufgabe 5
# Insert the correct syntax to assign values to multiple variables in one line:
x,y,z = "Orange","Banana","Cherry"
print(x,y,z)
# Alternative: print(x+y+z)

# Aufgabe 6
# Insert the correct syntax to assign the same value to all three variables in one code line.
x=y=z="Orange"
print(x)
print(y)
print(z)

# Aufgabe 7
# Insert the correct keyword to make the variable x belong to the global scope.
def myfunc():
    global x
    x= "fantastic"