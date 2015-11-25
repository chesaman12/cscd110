#Circle/Sphere Nate Elliott 10-21-15
import math

def main():
    radiusInfo(6.1)
    radiusInfo(7.5)
    radiusInfo(8)
    radiusInfo(11.25)
    radiusInfoUserInput()
    
def pi(): #function for exact pi value
    pi = math.pi
    return pi

def sphereSurfaceArea(radius):
    surfacearea = 4 * pi() * radius ** 2
    return surfacearea

def sphereVolume(radius):
    volume = 4/3 * pi() * radius ** 3
    return volume

def circleCircumference(radius):
    circumference = 2 * pi() * radius
    return circumference

def circleArea(radius):
    area = pi() * radius ** 2
    return area

def radiusInfo(radius):
    print("Surface area of Sphere of radius",radius,"is",sphereSurfaceArea(radius))
    print("Volume of Sphere of radius",radius,"is",sphereVolume(radius))
    print("Circumference of circle of radius",radius,"is",circleCircumference(radius))
    print("Area of circle of radius",radius,"is",circleArea(radius))
    print()

def radiusInfoUserInput():
    radius = float(input("Enter a radius: "))
    radiusInfo(radius)
    
main()

