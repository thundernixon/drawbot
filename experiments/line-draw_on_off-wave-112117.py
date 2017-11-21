currentLength = 0
fullLength = 800

lineEraserGap = 0

frames = 40
lines = 35
topLine = 900
bottomLine = 100

lineSpace = (topLine - bottomLine)/(lines - 1)

def wavyLines():
    for i in range(lines):
        # print bottomLine + i * lineSpace
        angle = 360 * i / lines
        angle += t * 360 # change this number to see wave move! 0 and 360 give the same result            
        currentLength = 250 + amplitude * sin(radians(angle+45)) 
        lineEraserGap  = 250 +  amplitude * sin(radians(angle))
        # short segment, gap that will grow, segment that will grow, full length of line
        lineDash(.1,lineEraserGap,currentLength,fullLength)
        y = bottomLine + i * lineSpace
        line((100, y), (900, y))
        line((899.9,y),(900,y))

for frame in range(frames):
    newPage(1000,1000) # set page size here to avoid a blank first page
    fill(0,0,.5)
    rect(0,0,1000,1000)
     # make stroke black
    strokeWidth(10) # make stroke 10px thick
    lineCap("round") # round endcaps
    # if it's the first half of the animation...

    amplitude = 250
    t = frame / frames
    
    blendMode("difference")

    stroke(1,0,0)
    wavyLines()
    
    rotate(180)
    translate(-1000,-1000)
    stroke(0,1,0)
    wavyLines()
    
saveImage("../exports/gifs/line-draw-8.gif")