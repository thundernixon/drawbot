from asciiDrawing import pixelOn;
from asciiDrawing import pixelOff;

####################################
# Layout logic below
####################################

def drawAscii(canvasWidth, canvasHeight, canvasMargin, asciiArt):
    ########## GET WIDTH OF ASCII ART

    # splitlines creates a list of strings, and max returns the longest string in a list
    longestRow = max(asciiArt.splitlines(), key=len)
    # check the answer
    print(longestRow)
    # count the letters in the longest row
    maxRowLength = len(longestRow)
    # check the answer
    print(maxRowLength)

    ########## GET HEIGHT OF ASCII ART

    # count number of rows
    numberOfRows = len(asciiArt.splitlines()) -1

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

    for row in asciiArt.splitlines():
        # start x at left side, with canvas margin
        pixelX = canvasMargin
        for pix in row:
            if pix == "x":
                # print if "yes pixel" (letter x in ASCII)
                # fill(.5,.5,1)
                # view total pixel size, including margins (uncomment to see it)
                # rect(pixelX,pixelY, pixelWidthOuter,pixelHeightOuter)
                # can you center whatever is passed in?
                pixelOn(pixelX+pixelMarginX,pixelY+pixelMarginY, pixelWidth, pixelHeight)
            else:
                # print if "no pixel"
                # fill(1,1,.5)
                pixelOff(pixelX+pixelMarginX,pixelY+pixelMarginY, pixelWidth,pixelHeight)
            pixelX = pixelX + pixelWidthOuter
        pixelY = pixelY - pixelHeightOuter
