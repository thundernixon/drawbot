currentLength = 0
fullLength = 2000

lineEraserGap = 0

frames = 10
lines = 35
topLine = 950
bottomLine = 50

lineSpace = (topLine - bottomLine)/(lines - 1)

def wavyLines():
    for i in range(lines):
        # print bottomLine + i * lineSpace
        angle = 360 * i / lines
        angle += t * 360 # change this number to see wave move! 0 and 360 give the same result            
        currentLength = 750 + amplitude * sin(radians(angle+45)) 
        lineEraserGap  = 750 +  amplitude * sin(radians(angle))
        # short segment, gap that will grow, segment that will grow, full length of line
        lineDash(.1,lineEraserGap,currentLength,fullLength)
        y = bottomLine + i * lineSpace
        line((100, y), (1900, y))
        line((1899.9,y),(100,y))

for frame in range(frames):
    newPage(2000,1000) # set page size here to avoid a blank first page
    fill(0,0,0)
    rect(0,0,2000,1000)
     # make stroke black
    strokeWidth(10) # make stroke 10px thick
    lineCap("round") # round endcaps
    # if it's the first half of the animation...

    amplitude = 650
    t = frame / frames
    countUpToOneHundred = 360 * t
    print "count up is ", countUpToOneHundred
    if frame < frames/2:
        countUpToOneHundred += t * sin(radians(countUpToOneHundred)) *.01
        blendMode("screen")
        print "t is ", t
        print "count up ", frame, "//", countUpToOneHundred
        print (countUpToOneHundred/2)*.01
        colorFactor = (countUpToOneHundred)*.01
        stroke(0+colorFactor,1-colorFactor,0)
    else:
        print (frame-(frames/2))*10
        # countUpToOneHundred -= (frame-(frames/2))*15
        countUpToOneHundred -= t * sin(radians(countUpToOneHundred)) *.01
        blendMode("screen")
        print "t is ", t
        print "count up ", frame, "//", countUpToOneHundred
        print (countUpToOneHundred/2)*.01
        colorFactor = (countUpToOneHundred)*.01
        
    print "\n"
    stroke(0+colorFactor,1-colorFactor,0)
    
    wavyLines()
    
    rotate(180)
    translate(-2000,-1000)
    stroke(0,0+colorFactor,1-colorFactor)
    # stroke(0,0,1)
    wavyLines()
    
# saveImage("../exports/gifs/line-draw-extrawide-3.mov")