currentLength = 0
fullLength = 800

lineEraserGap = 0

frames = 25
for frame in range(frames):
    newPage(1000,1000) # set page size here to avoid a blank first page
    stroke(0) # make stroke black
    strokeWidth(10) # make stroke 10px thick
    lineCap("round") # round endcaps
    # if it's the first half of the animation...
    if frame < frames/2:
        # increase currentLength variable
        currentLength += fullLength/frames*2
    # if it's the second half of the animation...
    else:
        # increase length of lineEraserGap variable
        lineEraserGap += fullLength/frames*2
        
    # short segment, gap that will grow, segment that will grow, full length of line
    lineDash(.1,lineEraserGap,currentLength,fullLength)
    
    # the line to draw
    line((100, 500), (900, 500))
    
saveImage("../exports/gifs/line-draw.gif")