# can you hide the complexity at the bottom of the code? maybe in a function? or maybe functions could surface the fun parts at the top?


canvasWidth = 1000
canvasHeight = 1000
canvasMargin = 50

# pixelSize = 40
# gridSize = 50

letter_a = """
.........
.x.x.x.x.
.x.x.x.x.
.xxx.x.x.
.x.x.x...
.x.x.x.x.
.........
"""

### do stuff for pixels that have "x" in ASCII art
def pixelOn(x,y,w,h):
    # set RGB color
    fill(0,0,1)
    # draw shape
    rect(x,y,w,h)
### do stuff for any other pixel in ASCII art    
def pixelOff(x,y,w,h):
    # set RGB color
    fill(1,.75,1)
    # draw shape
    oval(x,y,w,h)


####################################
# Layout logic below
####################################


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