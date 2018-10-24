def balls(x1,y1,r1, x2,y2,r2):
    if ((x2-x1)**2+(y2-y1)**2)**.5>r1+r2 :
        return False
    elif ((x2 - x1) ** 2 + (y2 - y1) ** 2)**.5 < abs(r2 - r1):
        return False
    else:
        return True

print(balls(4,1,5,4,1,2))