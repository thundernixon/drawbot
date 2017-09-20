import math

w = 1000
h = 1000
squares = 12



gridDistance = 162
squareSize = 120

frames = 50

for frame in range(frames):
    currentFrame = frame +1 # get number of current frame
    # set up black page
    newPage(w,h)
    frameDuration(.125)
    fill(0,0,0)
    rect(0,0,1000,1000)
    ## make condition for number of squares
    if currentFrame > (frames // 2): # if current frame is over half of total
        squares = squares - 1 # take current number of squares and shrink by one for each frame
        print "The frame is " + str(currentFrame) + " and there are " + str(squares) + " squares"
    else:
        squares = currentFrame # take current number of squares and grow by one for each frame
    # fill(1,1,1)
    # fontSize(30)
    # text("frame " + str(currentFrame), (20, 40))
    for i in range(squares):
        squareWidth = w/((squares * 2)+1)
        x = squareWidth + (i * squareWidth*2)
        for j in range(squares):
            fill(random()*(j+1), 0, random()*(j+1)/6)
            squareHeight = h/((squares * 2)+1)
            y = squareHeight + (j * squareHeight*2)
            if (i + j) % 2:
                rect(x, y, squareWidth, squareHeight)
            else:
                oval(x, y, squareWidth, squareHeight)
    # if frame > frames/2, 
    # squares = frame - (frames/2 + frame)

saveImage('../gifs/checkerboard-alt.gif')
