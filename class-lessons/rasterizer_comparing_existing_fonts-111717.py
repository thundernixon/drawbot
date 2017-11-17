
# prepare bezier paths. these won't change during animation
bezReg = BezierPath()
bezReg.text("A", font="InputSans-Bold", fontSize=27, offset=(0,0))

bezBold = BezierPath()
bezBold.text("A", font="Comic Sans MS", fontSize=27, offset=(0,0))

numFrames = 10

for frame in range(numFrames):

    newPage(500,500)
    scale(25)

    numPixels = 30
    diameter = 1.0

    for x in range(20):
        for y in range(20): 
            f = y / numPixels #between 1 and 0
            angle = 2 * pi * f
            diameter = 1 + 0.6 * (1 + sin(angle + 0.1))
            reg = bezReg.pointInside((x,y))
            bol = bezBold.pointInside((x,y))
            if reg and bol:
                fill(0,0,0)
                oval(x,y,diameter,diameter)
            elif bol:
                fill(0,0,1)
                oval(x,y,0.7*diameter,0.7*diameter)
            elif reg:
                fill(1,0,0)
                oval(x,y,0.4*diameter,0.4*diameter)
            else:
                fill(0,0,0)
                oval(x,y,0.1*diameter,0.1*diameter)
            