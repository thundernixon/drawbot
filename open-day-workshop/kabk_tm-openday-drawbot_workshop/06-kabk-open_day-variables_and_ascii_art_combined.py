Variable([
    dict(name="width", ui="Slider"),
    dict(name="height", ui="Slider"),
    dict(name="R", ui="Slider"),
    dict(name="G", ui="Slider"),
    dict(name="B", ui="Slider"),
    dict(name="alpha", ui="Slider"),
    dict(name="strokeThickness", ui="Slider"),
    ],globals())

asciiArt = """
---------
-x-x-xxx-
-x-x- x--
-xxx- x--
-x-x- x--
-x-x-xxx-
---------
"""


canvasWidth = 1000
canvasHeight = 1000
newPage(canvasWidth,canvasHeight)

canvasMargin = 50

# setting up: stroke thickness, stroke colour, fill colour
strokeWidth(strokeThickness)
stroke(0)
fill(R/100,G/100,B/100,alpha/100)


### do stuff for pixels that have "x" in ASCII art
def pixelOn():
    rect(100,100,100,height*10)
    # right stem
    rect(width*10,100,100,height*10)
    # middle bar
    rect(100,height*10/2+52,width*10,100)

    ##### I

    # moves the canvas to the right for the next shapes
    translate(width*10+100,0)

    # stem
    rect((width*10/2+52),100,100,height*10)
    # top bar
    rect(100,height*10+52-50,width*10,100)
    # bottom bar
    rect(100,100,width*10,100)
    print(width*10, width*5)

### do stuff for any other pixel in ASCII art    
def pixelOff():
    # set RGB color
    fill(1,1,1,.15)
    oval(450,450,100,100)





####################################################
# Layout logic below – only edit if you are brave
####################################################

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

    ## set up horizontal heights

    # divide the canvas horizontally by the longest row
    pixelWidthOuter = (canvasWidth - canvasMargin*2)/maxRowLength
    # get width for inside of pixel
    pixelWidth = pixelWidthOuter - (pixelWidthOuter/5)
    # get margin for left and right in pixels
    pixelMarginX = (pixelWidthOuter - pixelWidth) / 2
    
    ## set up vertical heights

    # divide the canvas vertically by the number of rows
    pixelHeightOuter = (canvasHeight - canvasMargin*2)/numberOfRows
    # get height for inside of pixel
    pixelHeight = pixelHeightOuter - (pixelHeightOuter/5)
    # get margin for top and bottom
    pixelMarginY = (pixelHeightOuter - pixelHeight)/2

    ## set up variables for positioning
    
    # we will draw pixels starting at the first row, so we set the top of our drawing area:
    pixelY = canvasHeight - canvasMargin
    # we set up a variable for x; we will update this with each row
    pixelX = 0
    
    ######## READ ASCII ART STRING, AND CALL "ON" AND "OFF" FUNCTIONS

    for row in asciiArt.splitlines():
        # start x at left side, with canvas margin
        pixelX = canvasMargin
        for pix in row:
            # print if "yes pixel" (the letter "x" in the ASCII art)
            if pix == "x":
                # view total pixel size, including margins (uncomment to see it)
                # rect(pixelX,pixelY, pixelWidthOuter,pixelHeightOuter)
            
                # the next two lines translate your shapes to the right place
                save()
                translate(pixelX+pixelMarginX,pixelY+pixelMarginY)
                scale(pixelWidth/canvasWidth, pixelHeight/canvasHeight)
                pixelOn()
                restore()
            
            # do if "no pixel"
            else:
                # print if "no pixel"
                # saves overall "state" (size and position) of canvas
                save()
                # translates pixel shapes to the right place
                translate(pixelX+pixelMarginX,pixelY+pixelMarginY)
                # scales pixel shapes to size of single pixel
                scale(pixelWidth/canvasWidth, pixelHeight/canvasHeight)
                pixelOff()
                #restores state of canvas
                restore()
            pixelX = pixelX + pixelWidthOuter
        pixelY = pixelY - pixelHeightOuter

# run the ascii logic function
drawAscii(canvasWidth, canvasHeight, canvasMargin, asciiArt)