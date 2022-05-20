import math 
  
def checkPoint(radius, x, y, percent, startAngle): 
    endAngle = 360 * percent/100 + startAngle 
  
    if x >=0:
        polarradius = math.sqrt(x * x + y * y)
    elif x < 0:
        x = -x
        polarradius =  math.sqrt(x * x + y * y)

    if x == 0:
        Angle = 90

    if y >=0:
        polarradius = math.sqrt(x * x + y * y)
    elif y < 0:
        y = -y
        polarradius =  math.sqrt(x * x + y * y)

    if y == 0:
        Angle = 90

    
    else:
        Angle = math.atan(y / x)

    if (Angle >= startAngle and Angle <= endAngle and polarradius <= radius and polarradius >=0 ):
        print("Point (", x, ",", y, ") exist in the circle sector") 
    else: 
        print("Point (", x, ",", y, ") does not exist in the circle sector") 
  
radius, x, y = 8, 3, -4
percent, startAngle = 50, 0
  
checkPoint(radius, x, y, percent, startAngle)



#if up >>> then |x|  , y = +  , down >>> then x = +,- , y = - 
