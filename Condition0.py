def  circle_area(r):
    area = 3.14*r**2
    return area
def square_area(side):
    area = side**2
    return area
def rectangle_area(l,w):
    area = l*w
    return area
def triangle_area(b,h):
    area = 0.5*b*h
    return area
req = input("Enter the shape you wish to see area for:")
if req == "square":
  side = int(input("Enter side:"))
  ans1 = square_area(side)
  print(ans1)
elif req == "rectangle":
    l, w = map(int, input("Enter the length and breadth (with space): ").split())
    ans2 = rectangle_area(l, w)
    print(ans2)
elif req == "triangle":
    b, h = map(int, input("Enter the height and breadth (with space): ").split()) 
    ans3 = triangle_area(b,h)
    print(ans3)
elif req == "circle":
    r = int(input("Enter the r:"))
    ans4 = circle_area(r)
    print(ans4)
else:
    print("Error")
req = input("Enter the shape you wish to see area for:")    
    