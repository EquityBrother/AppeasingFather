from math import pi, pow

radius = int(input("What is the radius (in cm) of the sphere?\n"))

volume = 4/3 * pi * pow(radius, 3)

print(f"A sphere with radius {radius} has volume {volume:.2f} cm^3.")