import math

w = 1000
h = 1000
squares = 12

frames = 60

#  interpolate colors

def interpolate(a, b, t):
    interAB = a*(1-t) + b*t
    return interAB
    
colorA = (1,1,0)
colorB = (1,0,1)

for frame in range(frames):
    currentFrame = frame + 1 # get number of current frame
    # set up each new page
    newPage(w,h)
    frameDuration(.125)
    # fill(0+((1/frames)*frame),0+(((1/frames)*frame)/2),0) # background black to orange
    # fill(0,1-((1/frames)*frame),0) # background green to black

    rect(0,0,1000,1000)
    ## make condition for number of squares
    if currentFrame > (frames // 2): # if current frame is over half of total
        squares = squares - 1 # take current number of squares and shrink by one for each frame
        rotate(90)
        translate(0,-h)
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
            if (i + j) % 2:
                fill( interpolate( colorA[0] , colorB[0], t * random() ), interpolate(colorA[1] * random() *.5, colorB[1], t * random()), interpolate(colorA[2], colorB[2], t * random()), 1)
                rect(x, y, squareWidth, squareHeight)
            else:
                fill( interpolate( colorB[0], colorA[0], t * random() ), interpolate(colorB[1] * random() *.5, colorA[1], t * random()), interpolate(colorB[2], colorA[2], t * random()), 1)
                oval(x-.5*(circleWidth-squareWidth), y-.5*(circleWidth-squareWidth), circleWidth, circleWidth)

# saveImage('../gifs/checkerboard-alt-6.gif')
