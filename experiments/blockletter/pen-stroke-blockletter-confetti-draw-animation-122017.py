from letters import *

def drawStroke(pointA,pointB,angle, strokeWidth):
    # rect with pointA as center, rotated to angle
    save()
    translate(pointA[0],pointA[1])
    rotate(angle)
    translate(-pointA[0],-pointA[1])

    rect(pointA[0]-strokeWidth/2, pointA[1]-lineThickness/2, strokeWidth,lineThickness)
    restore()
    
    save()
    translate(pointB[0],pointB[1])
    rotate(angle)
    translate(-pointB[0],-pointB[1])
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
            
def path_a():
    letterWidth = 272
    strokes = [
        
        ((16, 186), (96, 162),  45, 46), # left bottom serif
        ((102, 347), (76, 207), 205, 46), # left stem
        ((54, 387), (208, 372), 65, 46), # top bar
        ((180, 340), (216, 214), 205, 46), # right stem
        ((180, 186), (242, 174), 45, 46), # right bottom serif
        ((124, 276), (158, 256), 45, 46) # central crossbar
        ]
    return strokes, letterWidth    

def path_b():
    letterWidth = 240
    strokes = [
        ((70, 392), (106, 210), 205, 46),
        ((46, 180), (182, 176), 57, 46),
        ((114, 374), (216, 394), 57, 46),
        ((228, 379), (205, 321), 196, 46),
        ((128, 296), (224, 290), 57, 46),
        ((236, 271), (218, 200), 8, 46),
    ]
    return strokes, letterWidth
    
# def path_d():
#     letterWidth = 240
#     strokes = [
#         ((76, 346), (96, 210), 221, 46),
#         ((36, 181), (164, 172), 45, 46),
#         ((197, 342), (198, 208), 221, 46),
#         ((55, 381), (229, 374), 45, 46)
#     ]
#     return strokes, letterWidth 

def path_d():
    letterWidth = 240
    strokes = [
        ((110, 349), (123, 207), 221, 46), # main stem
        ((36, 181), (171, 165), 45, 46), # bottom
        ((199, 350), (208, 194), 211, 46), # right of bowl
        ((45, 387), (231, 382), 54, 46), # top bar
        ((54, 324), (64, 234), 221, 46) # left decorator
    ]
    return strokes, letterWidth 

def path_k():
    letterWidth = 240
    strokes = [
        ((76, 346), (104, 213), 221, 46),
        ((134, 168), (46, 186), 45, 46),
        ((176, 384), (104, 382), 65, 46),
        ((133, 260), (216, 222), 54, 46),
        ((152, 300), (236, 302), 76, 44),
        ((193, 182), (244, 171), 65, 46),
    ]
    return strokes, letterWidth
    
def path_r():
    letterWidth = 240
    strokes = [
        ((76, 346), (88, 207), 221, 46),
        ((36, 176), (122, 172), 45, 46),
        ((100, 386), (38, 386), 65, 46),
        ((110, 352), (162, 381), -125, 46), # connection to top of bowl
        ((200, 406), (170, 314), 17, 46), # right of bowl
        ((130, 292), (209, 218), 38, 46), # leg
        ((183, 182), (244, 171), 65, 46), # leg serif
    ]
    return strokes, letterWidth
    
def path_w():
    letterWidth = 240
    strokes = [
        ((8, 386), (70, 386),  65, 46), # left top serif
        ((42, 352), (48, 205), 211, 46), #left stem
        ((14, 176), (85, 174), 45, 46), # bottom of left
        ((115, 373), (121, 203), 211, 46), #middle stem
        ((119, 174), (184, 176), 135, 46), # bottom of right
        ((202, 352), (190, 203), 211, 46), #middle stem
        ((168, 386), (230, 386), 65, 46), # right top serif
    ]
    return strokes, letterWidth

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
    "d": path_d(),
    "k": path_k(),
    "r": path_r(),
    "w": path_w(),
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


frameNum = 30
lineThickness = 2

rand1 = 0
rand2 = 0
randFactor = 1.5

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
    fill(0,0,0)
    rect(0,0,1000,1000)
    fill(.569, .082, 1,.25)
    rect(0,0,1000,1000)
    translate(10,0)
    fill(.569, .082, 1)
    
    angle = 0
        
    if frame < frameNum/2:
        # angle += sin(360/frameNum * (frame*0.125))
        scaleUp += scaleFactor
        print angle
        scale(currentScale*.01 + scaleUp*.01) # 500,500
        # translate(-scaleUp*2,-scaleUp*2)
        rand1 += sin(-decreaseRand1) * randFactor
        rand2 += sin(decreaseRand2) * randFactor
        # print int(rand2)

    else:
        # angle -= sin(360/frameNum * (frame*0.125))
        angle -= frameNum 
        scaleUp -= scaleFactor
        print angle
        scale(currentScale*.01 + scaleUp*.01)
        # translate(-scaleUp*2,-scaleUp*2)
        rand1 += sin(decreaseRand1) * randFactor
        rand2 -= sin(decreaseRand2) * randFactor
        
    # lineThickness = frameNum*cos(frame*5+50)
    
        
    drawLetterPaths("draw", rand1, rand2)
        
saveImage("../../exports/gifs/blockletter-draw-4-122017.gif")



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

