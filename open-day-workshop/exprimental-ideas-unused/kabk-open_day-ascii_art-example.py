import asciiDrawingLogic;


canvasWidth = 1000
canvasHeight = 1000
canvasMargin = 50

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
    
drawAscii()