# import drawAscii() from asciiDrawingLogic;


canvasWidth = 1600
canvasHeight = 900
canvasMargin = 50



letter_a = """
-------------
-x--x-xxx-x--
-x--x--x--x--
-xxxx--x--x--
-x--x--x-----
-x--x-xxx-x--
-------------
"""



for i in range(5):
    newPage(canvasWidth,canvasHeight)
    rect(0,0,canvasWidth, canvasHeight)
    ### do stuff for pixels that have "x" in ASCII art
    def pixelOn(x,y,w,h):
        # the next two lines translate your shapes to the right place
        save()
        translate(x,y)
        # rect(x,y,w,h)
    
        for i in range(50):
            fill(0,0,.75-(i/50),1-(i/50))
            rect(2*i,-2*i,w,h)
        # set RGB color
        fill(0,0,1)
        # draw shape
        rect(0,0,w,h)
        # this restores the overall canvas coordinates
        restore()
    
    ### do stuff for any other pixel in ASCII art    
    def pixelOff(x,y,w,h):
        # the next two lines translate your shapes to the right place
        save()
        translate(x,y)
    
        for i in range(50):
            fill(1,.5,1,(.15-(i/50)))
            oval(2*i,-2*i,w,h)
        # set RGB color
        fill(randint(1,10)*.01*1,randint(1,10)*.01*.75,randint(1,10)*.01*1,.5)
        # draw shape
        oval(0,0,w,h)
    
        # this restores the overall canvas coordinates
        restore()
    

    ####################################
    # Layout logic below
    ####################################

    def drawAscii():
        ########## GET WIDTH OF ASCII ART

        # splitlines creates a list of strings, and max returns the longest string in a list
        longestRow = max(letter_a.splitlines(), key=len)
        # check the answer
        print(longestRow)
        # count the letters in the longest row
        maxRowLength = len(longestRow)
        # check the answer
        print(maxRowLength)

        ########## GET HEIGHT OF ASCII ART

        # count number of rows
        numberOfRows = len(letter_a.splitlines()) -1

        ########## SET UP PIXEL SIZE
        # availableCanvas = canvasMargin / 2

        # divide the canvas horizontally by the longest row
        pixelWidthOuter = (canvasWidth - canvasMargin*2)/maxRowLength
        # get width for inside of pixel
        pixelWidth = pixelWidthOuter - (pixelWidthOuter/5)
        # get margin for left and right in pixels
        pixelMarginX = (pixelWidthOuter - pixelWidth) / 2

        # pixelSideMargin = 

        # divide the canvas vertically by the number of rows
        pixelHeightOuter = (canvasHeight - canvasMargin*2)/numberOfRows
        # get height for inside of pixel
        pixelHeight = pixelHeightOuter - (pixelHeightOuter/5)
        # get margin for top and bottom
        pixelMarginY = (pixelHeightOuter - pixelHeight)/2

        ######## set up height of inner composition

        # we will draw pixels starting at the first row, so we set the top of our drawing area:
        pixelY = canvasHeight - canvasMargin
        # we set up a variable for x; we will update this with each row
        pixelX = 0

        for row in letter_a.splitlines():
            # start x at left side, with canvas margin
            pixelX = canvasMargin
            for pix in row:
                if pix == "x":
                    # print if "yes pixel" (letter x in ASCII)
                    fill(.5,.5,1)
                    # view total pixel size, including margins (uncomment to see it)
                    # rect(pixelX,pixelY, pixelWidthOuter,pixelHeightOuter)
                    # can you center whatever is passed in?
                    pixelOn(pixelX+pixelMarginX,pixelY+pixelMarginY, pixelWidth, pixelHeight)
                else:
                    # print if "no pixel"
                    fill(1,1,.5)
                    pixelOff(pixelX+pixelMarginX,pixelY+pixelMarginY, pixelWidth,pixelHeight)
                pixelX = pixelX + pixelWidthOuter
            pixelY = pixelY - pixelHeightOuter
    
    drawAscii()
    
saveImage("hi.gif")