# Program to calculate the area of various shapes

# Calculates the area of a shape
def calculate_area(shape):
    area = 0
    # Circle
    if shape == 'C':
        radius = input("Enter the radius: ")
        area = calculate_circle_area(float(radius))
    elif shape == 'S':
        side = input("Enter the side: ")
        area = calculate_square_area(float(side))
    elif shape == 'R':
        length = input("Enter the length: ")
        width = input("Enter the width: ")        
        area = calculate_rectangle_area(float(length), float(width))
    else:
        print("Invalid selection. Choose 'C', 'S' or 'R'.")

    return area

# Calculates the area of a square
def calculate_square_area(side: float):
    area = side * side
    return area

# Calculates the area of a rectangle with given length and width
def calculate_rectangle_area(length: float, width: float):
    area = length * width
    return area

# Calculates the area of a circle
def calculate_circle_area(radius: float):
    pi = 3.14
    area = pi * radius ** 2
    return area

# Returns the name of the shape matching the selection
def get_shape_name(tag):
    shape = "Unknown"
    if tag == 'C':
        shape = "circle"        
    elif tag == 'S':
        shape = "square"
    elif tag == 'R':
        shape = "rectangle"
    return shape

# Testing
print("""
---------------
Area calculator
---------------
Select a shape:
""")

# Prompt the user to select a shape and wait
selection = input("""\t'S' - Square
\t'R' - Rectangle
\t'C' - Circle
""")

area = -1
# Square
if selection == 'S':
    side = input("Enter the side: ")
    area = calculate_square_area(float(side))
# Rectangle
elif selection == 'R':
    length = input("Enter the length: ")
    width = input("Enter the width: ")        
    area = calculate_rectangle_area(float(length), float(width))
# Circle    
elif selection == 'C':
    radius = input("Enter the radius: ")
    area = calculate_circle_area(float(radius))
else:
    print("Invalid selection. Choose 'S', 'R' or 'C'.")

print(f"The area is {area}")
