import math
radi = float(input("Enter the radius of a circle in cm: "))

#diameter func.
def diameter(radi):
    return radi*2.0
#circumference func.
def circum(radi):
    return 2*radi*math.pi
#area
def area(radi):
    return math.pi*radi**2

print(f"The diameter of the circle in cm is {diameter(radi):.2f}")
print(f"The circumference of the circle in cm is {circum(radi):.2f}")
print(f"The area of the circle in cm is {area(radi):.2f}")