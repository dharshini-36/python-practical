#find the area of rectangle, square, triangle and circle

#area of rectangle
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
area_rec=l*b
print(f"The area of the rectangle is: {area_rec}")

#area of square
s=int(input("Enter the side of the square:"))
area_sq=s*s
print(f"The area of the square is: {area_sq}")

#area of triangle
b=int(input("Enter the base of the triangle:"))
h=int(input("Enter the height of the triangle:"))
area_tri=1/2*b*h
print(f"The area of the triangle is: {area_tri}")

#area of circle
pi=3.14
r=int(input("Enter the radius of the circle:"))
area_cir=pi*r*r
print(f"The area of the circle is: {area_cir}")
