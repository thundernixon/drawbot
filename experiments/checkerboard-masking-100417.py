import math

w = 1000
h = 1000
squares = 12

frames = 90

#  interpolate colors

def interpolate(a, b, t):
    interAB = a*(1-t) + b*t
    return interAB
    
colorA = (0,1,1)
colorB = (1,0,1)

# animation

for frame in range(frames):
    currentFrame = frame + 1 # get number of current frame
    # set up black page
    newPage(w,h)
    
    save()
    translate(x=0, y=-100)
    
    # ////////// shape ///////////

    bez = BezierPath()

    # big shape
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
        (342, 178) # endpoint
        )
    bez.curveTo(
        (468, 174), # handle one
        (552, 226), # handle two
        (600, 300) # endpoint
        )
    bez.lineTo((600, 402))
    bez.curveTo(
        (520, 308), # handle one
        (466, 296), # handle two
        (436, 296) # endpoint
        )
    bez.curveTo(
        (400, 292), # handle one
        (364, 312), # handle two
        (364, 350) # endpoint
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
        
    fill(None)
    stroke(None)
    strokeWidth(10)
    drawPath(bez)

    # ////////// END shape //////////
    
    restore()
    
    frameDuration(.125)
    # fill(0+((1/frames)*frame),0+(((1/frames)*frame)/2),0) # black to orange
    # fill(0,1-((1/frames)*frame),0) # black to red
    fill(0)

    rect(0,0,1000,1000)
    ## make condition for number of squares
    if currentFrame > (frames // 2): # if current frame is over half of total
        squares = squares - 1 # take current number of squares and shrink by one for each frame
        # rotate(90)
        # translate(0,-h)
    else:
        squares = currentFrame # take current number of squares and grow by one for each frame
    for i in range(squares):
        squareWidth = w/((squares * 2)+1)
        circleWidth = squareWidth + (squareWidth*.15)
        x = squareWidth + (i * squareWidth*2)
        for j in range(squares):
            t = i/squares
            
            # fill(random()*(j+1/currentFrame), 0, random()*(j+1)/currentFrame+currentFrame, .75)
            squareHeight = h/((squares * 2)+1)
            y = squareHeight + (j * squareHeight*2)
            if bez.pointInside((x,y)):
                    fill(1)
            else:
                fill( interpolate( colorA[0] , colorB[0], t * random() ), interpolate(colorA[1] * random() *.5, colorB[1], t * random()), interpolate(colorA[2], colorB[2], t * random()), .5)
            rect(x, y, squareWidth, squareHeight)

saveImage('../gifs/checkerboard-a-masking.gif')
