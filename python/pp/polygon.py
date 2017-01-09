import math

poly = int(raw_input("Enter the number of side on a polygon you like: "))

diagonals = poly * (poly - 3) / 2

print "The number of diagonals within your", poly, "sides's polygon is ", diagonals


side1 = int(raw_input("Etner the length of the first side of your right-angle triangle: "))
side2 = int(raw_input("Etner the length of the second side of your right-angle triangle: "))

hypotenuse = math.sqrt(side1*side1+side2*side2)

print "The length of your right-angle triangle's hypotenuse is ", hypotenuse
