fill(.75)
rect(0,0,1000,300)

# save()
# translate(x=0, y=-50)

bez = BezierPath()

# big shape
bez.moveTo((200, 650))
bez.curveTo(
    (200, 888), # handle one
    (428, 900), # handle two
    (500, 900) # endpoint
    )
bez.curveTo(
    (750, 900), # handle one
    (800, 750), # handle two
    (800, 650) # endpoint
    )
bez.lineTo((800, 300))
bez.curveTo(
    (800, 275), # handle one
    (800, 240), # handle two
    (850, 240) # endpoint
    )
bez.lineTo((850, 200))
bez.lineTo((600, 200))
bez.lineTo((600, 650))
bez.curveTo(
    (600, 699), # handle one
    (585, 750), # handle two
    (492, 750) # endpoint
    )
bez.curveTo(
    (426, 749), # handle one
    (392, 712), # handle two
    (392, 650) # endpoint
    )
bez.closePath()

# //// bowl /////

bez.moveTo((600, 576))
bez.lineTo((406, 540))
bez.curveTo(
    (268, 511), # handle one
    (154, 472), # handle two
    (160, 326) # endpoint
    )
bez.curveTo(
    (160, 179), # handle one
    (312, 178), # handle two
    (348, 178) # endpoint
    )
bez.curveTo(
    (468, 178), # handle one
    (552, 226), # handle two
    (600, 300) # endpoint
    )
bez.lineTo((600, 402))
bez.curveTo(
    (520, 308), # handle one
    (466, 296), # handle two
    (418, 296) # endpoint
    )
bez.curveTo(
    (392, 296), # handle one
    (364, 312), # handle two
    (364, 346) # endpoint
    )
bez.curveTo(
    (364, 376), # handle one
    (362, 412), # handle two
    (458, 438) # endpoint
    )
bez.lineTo((600, 472))
bez.closePath()

bez.moveTo((200, 125))
bez.lineTo((800, 125))
bez.lineTo((800, 75))
bez.lineTo((200, 75))
bez.closePath()

fill(1,0,0)
stroke(0)
strokeWidth(10)
drawPath(bez)



print bez.pointInside((534, 830))

x, y =(498, 390)
if bez.pointInside((x,y)):
    fill(0,0,1)
else:
    fill(1,0,0)
    
stroke(None)
rect(x,y,15,15)

stroke(0)
strokeWidth(2)
fill(None)
print bez.bounds()
x,y,cx,cy = (bez.bounds())

rect(x,y,cx,cy)

# restore()