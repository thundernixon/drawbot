currentLength = 0
fullLength = 800

lineEraserGap = 0

frames = 20
lines = 90
topLine = 900
bottomLine = 100
startLength = 200

lineSpace = (topLine - bottomLine)/(lines - 1)

def wavyLines():
    for i in range(lines):
        # print bottomLine + i * lineSpace
        angle = 360 * i / lines
        angle += t * 360 # change this number to see wave move! 0 and 360 give the same result            
        currentLength = startLength + amplitude * sin(radians(angle+45)) 
        lineEraserGap  = startLength +  amplitude * sin(radians(angle))
        # short segment, gap that will grow, segment that will grow, full length of line
        lineDash(.1,lineEraserGap,currentLength,fullLength)
        y = bottomLine + i * lineSpace
        line((100, y), (900, y))
        line((899.9,y),(900,y))

for frame in range(frames):
    newPage(1000,1000) # set page size here to avoid a blank first page
    fill(0,0,0)
    rect(0,0,1000,1000)
     # make stroke black
    strokeWidth(2) # make stroke 10px thick
    lineCap("round") # round endcaps
    # if it's the first half of the animation...

    amplitude = 300
    t = frame / frames
    
    blendMode("screen")

    stroke(1,.35)
    wavyLines()
    
    rotate(90)
    translate(0,-1000)
    stroke(1,.35)
    wavyLines()
    
    rotate(90)
    translate(0,-1000)
    stroke(1,.35)
    wavyLines()
    
    rotate(90)
    translate(0,-1000)
    stroke(1,.35)
    wavyLines()
    
saveImage("../exports/gifs/line-draw-13.gif")