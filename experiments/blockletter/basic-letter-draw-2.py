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
        
        ((126, 162), (46, 186), 45, 46), # left bottom serif
        ((132, 344), (106, 210), 205, 46), # left stem
        ((164, 377), (238, 372), 65, 46), # top bar
        ((210, 340), (246, 214), 205, 46), # right stem
        ((210, 186), (272, 174), 45, 46), # right bottom serif
        ((154, 276), (188, 256), 45, 46) # central crossbar
        ]
    return strokes, letterWidth   

def path_d():
    letterWidth = 240
    strokes = [
        ((110, 349), (123, 212), 221, 46),
        ((36, 181), (161, 172), 45, 46),
        ((197, 348), (198, 201), 211, 46),
        ((45, 387), (231, 378), 45, 46),
        ((54, 324), (64, 234), 221, 46)
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
        ((100, 386), (38, 386), 65, 46), # left top serif
        ((72, 352), (68, 205), 211, 46), #left stem
        ((34, 176), (105, 174), 45, 46), # bottom of left
        ((142, 373), (141, 203), 211, 46), #middle stem
        ((139, 174), (204, 176), 135, 46), # bottom of right
        ((222, 352), (210, 203), 211, 46), #middle stem
        ((200, 386), (250, 386), 65, 46), # right top serif

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
    
lineThickness = 2
    
fontPathDictionary = {
    "a": path_a(),
    "d": path_d(),
    "k": path_k(),
    "r": path_r(),
    "w": path_w(),
    }
def drawLetterPaths(txt):
    cursor = 0
    translate(20, 160)
    for char in txt:

        letter = fontPathDictionary.get(char, missing_glyph())
    
        for stroke in letter[0]:
            # rand1 += -rand1/frameNum
            # print rand1
            # rand2 -= rand2/frameNum
            # pointA, pointB = stroke[0], stroke[1]
            # print pointA[0]*randint(2,3)

            # print "rand1 is " + str(rand1)
            # print "rand2 is " + str(rand2)
            drawStroke(stroke[0], stroke[1], stroke[2], stroke[3])
        if cursor > 200:
            cursor = 0
            translate(-240, -290)
            # print "cursor is " + str(cursor)
        else:
            translate(letter[1],0)
            cursor += letter[1]
            # print "cursor is " + str(cursor)
            
drawLetterPaths("draw")