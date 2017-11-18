from letters import *

def drawStroke(pointA,pointB,angle, strokeWidth):
    # rect with pointA as center, rotated to angle
    save()
    translate(pointA[0],pointA[1])
    rotate(angle)
    translate(-pointA[0],-pointA[1])
    # fill(0.8,0.8,1)
    # rect(0,0,500,500)
    # fill(0,0,1)f
    rect(pointA[0]-strokeWidth/2, pointA[1]-lineThickness/2, strokeWidth,lineThickness)
    restore()
    
    save()
    translate(pointB[0],pointB[1])
    rotate(angle)
    translate(-pointB[0],-pointB[1])
    # fill(1,0,0)
    rect(pointB[0]-strokeWidth/2, pointB[1]-lineThickness/2, strokeWidth,lineThickness)
    restore()
    
    distance = sqrt((pointB[0]-pointA[0])*(pointB[0]-pointA[0]) + (pointB[1]-pointA[1])*(pointB[1]-pointA[1]))
    
    # print "distance is " + str(distance)
    
    divisions =  int(distance / (lineThickness*2))
    
    for div in range(divisions):
        currentT = (1/divisions) * div
        # print currentT
        t = currentT*distance / distance
        x = ((1 - t) * pointA[0]) + (t * pointB[0])
        y = ((1 - t) * pointA[1]) + (t * pointB[1])

        if currentT > 0:
            save()
            translate(x,y)
            rotate(angle)
            translate(-x,-y)
            rect(x-strokeWidth/2, y-lineThickness/2, strokeWidth,lineThickness)
            restore()

def missing_glyph():
    letterWidth = 240
    strokes = [
        ((85, 346), (85, 195), 80, 46),
        ((80, 200),(210, 200), 10, 46),
        ((205, 346), (205, 195), 80, 46),
        ((80, 345),(210, 345), 10, 46),
        ((114, 229),(174, 315), 41, 46),
        ((174, 229),(114, 315), -41, 46),
    ]
    return strokes, letterWidth
    
fontPathDictionary = {
    "a": path_a(),
    "b": path_b(),
    "k": path_k(),
    }





def drawLetterPaths(txt, rand1, rand2):
    cursor = 0
    translate(20, 160)
    for char in txt:

        letter = fontPathDictionary.get(char, missing_glyph())
    
        for stroke in letter[0]:
            # rand1 += -rand1/frameNum
            # print rand1
            # rand2 -= rand2/frameNum
            pointA, pointB = stroke[0], stroke[1]
            # print pointA[0]*randint(2,3)

            # print "rand1 is " + str(rand1)
            # print "rand2 is " + str(rand2)
            drawStroke(
                (pointA[0]-rand2*randint(-4,4), pointA[1]-rand2*randint(-4,4)),
                (pointB[0]+rand1*randint(-4,4), pointB[1]+rand1*randint(-4,4)),
                stroke[2]+(rand1),
                stroke[3])
        

        
        if cursor > 200:
            cursor = 0
            translate(-240, -290)
            # print "cursor is " + str(cursor)
        else:
            translate(letter[1],0)
            cursor += letter[1]
            # print "cursor is " + str(cursor)


frameNum = 20
lineThickness = 2

rand1 = 0
rand2 = 0

# decreaseRand1 = randint(-300,-50)/frameNum
# decreaseRand2 = randint(100,300)/frameNum

decreaseRand1 = -300
decreaseRand2 = 300

currentScale = 85
scaleUp = 0
scaleFactor = 0

for frame in range(frameNum):
    
    # newPage(1000,1000) 
    newPage(500,500) 
    
    # scale(1.7) # 1000, 1000
    
    # frameDuration(.25)
    fill(0,0,1)
    rect(0,0,1000,1000)
    fill(1,1,1)
    
    angle = 0
        
    if frame < frameNum/2:
        # angle += sin(360/frameNum * (frame*0.125))
        scaleUp += scaleFactor
        print angle
        scale(currentScale*.01 + scaleUp*.01) # 500,500
        # translate(-scaleUp*2,-scaleUp*2)
        rand1 += sin(-decreaseRand1)
        rand2 += sin(decreaseRand2)
        # print int(rand2)

    else:
        # angle -= sin(360/frameNum * (frame*0.125))
        angle -= frameNum 
        scaleUp -= scaleFactor
        print angle
        scale(currentScale*.01 + scaleUp*.01)
        # translate(-scaleUp*2,-scaleUp*2)
        rand1 += sin(decreaseRand1)
        rand2 -= sin(decreaseRand2)
        
    # lineThickness = frameNum*cos(frame*5+50)
    
        
    drawLetterPaths("kabk", rand1, rand2)
        
saveImage("../../exports/gifs/blockletter-kabk-19-111717.gif")



########### NOTES ###########

# start as normal letters
# incrementally randomize coordinates; first quickly and then more slowly
# after half the frames have elapsed, start to make coordinates less random (reverse explosion)

# currently, this isn't random ... coordinates are just moving one way, then back. but a prior attempt to make it random made it just wobble. I need some way to randomize this onto different pieces of each letter...

#####

# to use this pen tool on bezier paths, the math looks like...
# x1,y1 = P1
# x2,y2 = P2
# x3,y3 = P3
# x4,y4 = P4
# x = x1*(1-t)**3 + x2*3*t*(1-t)**2 + x3*3*t**2*(1-t) + x4*t**3
# y = y1*(1-t)**3 + y2*3*t*(1-t)**2 + y3*3*t**2*(1-t) + y4*t**3

