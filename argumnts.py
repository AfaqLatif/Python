def cylinder_volume(radius,height=1):
    print("radius is:",radius)
    print("height is:",height)
    area = 3.14*(radius**2)*height
    return area

#positional vs named arguments
r=5
h=10
print(cylinder_volume(height=h,radius=r))

# default arguments
r=5
h=10
print(cylinder_volume(radius=r))