from asciiDrawingLogic import drawAscii;

asciiArt = """
-------
-x-x-x-
-x-x-x-
-xxx-x-
-x-x-x-
-x-x-x-
-------
"""


canvasWidth = 1000
canvasHeight = 1000
newPage(canvasWidth,canvasHeight)

canvasMargin = 50

# set color to black
fill(0,0,0)
# make rectangle for background
rect(0,0,canvasWidth, canvasHeight)

### do stuff for pixels that have "x" in ASCII art
def pixelOn():
    fill(0,0,.25)
    rect(200,200,500,500)
    fill(0,0,1)
    rect(400,400,500,500)

### do stuff for any other pixel in ASCII art    
def pixelOff():
    # set RGB color
    fill(1,1,1,.15)
    oval(450,450,100,100)

drawAscii(canvasWidth, canvasHeight, canvasMargin, asciiArt)