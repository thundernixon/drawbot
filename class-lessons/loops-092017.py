import math

w = 1000
h = 1000
squares = 12



gridDistance = 162
squareSize = 120

frames = 6

for frame in range(frames):
    currentFrame = frame +1 # get number of current frame
    # set up black page
    newPage(w,h)
    frameDuration(.25)
    fill(0,0,0)
    rect(0,0,1000,1000)
    ## make condition for number of squares
    if frame >= (frames / 2): # if current frame is over half of total
        # decreasingFrame = (frame - 1) - (frames // 2) # double divide gives and integer
        squares = currentFrame - (frames // 2)
            # frame 4 minus 1 is 3 squares
            # frame 5 minus 3  is 2 squares
            # frame 6 minus 5 is 1 square
        print "The frame is " + str(frame + 1) + " and there are " + str(squares) + " squares"
    else:
        squares = currentFrame
    
    fill(1,1,1)
    fontSize(30)
    text("frame " + str(currentFrame), (20, 40))
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

# saveImage('../gifs/checkerboard.gif')
