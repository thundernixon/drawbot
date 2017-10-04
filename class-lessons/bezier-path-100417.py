fill(.75)
rect(0,0,1000,300)

bez = BezierPath()

# big shape
bez.moveTo((200, 650))
bez.curveTo(
    (200, 850), # handle one
    (428, 900), # handle two
    (500, 900) # endpoint
    )
bez.curveTo(
    (750, 900), # handle one
    (800, 750), # handle two
    (800, 650) # endpoint
    )
bez.lineTo((800, 200))
bez.lineTo((600, 200))
bez.lineTo((600, 650))
bez.curveTo(
    (600, 699), # handle one
    (585, 750), # handle two
    (500, 750) # endpoint
    )
bez.curveTo(
    (426, 749), # handle one
    (400, 712), # handle two
    (400, 650) # endpoint
    )
bez.closePath()

# //// bowl /////

bez.moveTo((625, 550))
bez.lineTo((400, 500))
bez.curveTo(
    (600, 699), # handle one
    (585, 750), # handle two
    (500, 750) # endpoint
    )

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