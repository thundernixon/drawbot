def triangle(x,y,w,h):
    polygon(
        (x,y),
        (x + w/2, y +h),
        (x + w, y)   
    )
    
rn = randint(1,3)

if rn == 1:
    shape = triangle
elif rn == 2:
    shape = rect
else:
    shape = oval
        
shape(150,150,300,400)