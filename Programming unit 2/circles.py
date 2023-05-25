from math import pi

def circle_length(r):
    circle=r*pi*2
    return circle
def circle_area(r):
    area=pi*r**2
    return area
r=input('Circle radius: ')
r=float(r)
print('Circumference is: ', circle_length(r))
print('Area is: ', circle_area(r))
