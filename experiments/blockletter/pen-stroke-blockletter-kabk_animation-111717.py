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

newPage(500,500)

lineThickness = 3

# drawstroke = drawstroke.drawStroke
        
def path_a():
    letterWidth = 272
    strokes = [
        ((132, 344), (106, 210), 205, 46),
        ((126, 162), (46, 186), 45, 46),
        ((164, 377), (238, 372), 65, 46),
        ((210, 340), (246, 214), 205, 46),
        ((210, 186), (272, 174), 45, 46),
        ((154, 276), (188, 256), 45, 46)
        ]
    # def shapes():
    #     drawStoke((132, 344), (106, 210), 205, 46)
    #     drawStoke((126, 162), (46, 186), 45, 46)
    #     drawStoke((164, 377), (238, 372), 65, 46)
    #     drawStoke((210, 340), (246, 214), 205, 46)
    #     drawStoke((210, 186), (272, 174), 45, 46)
    #     drawStoke((154, 276), (188, 256), 45, 46)
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
    

# path_a()

# path_b()

def missing_glyph():
    letterWidth = 192
    path = BezierPath()
    path.moveTo((66, 424))
    path.lineTo((66, 156))
    path.lineTo((166, 156))
    path.lineTo((166, 422))
    path.closePath()
    return path, letterWidth
    
fontPathDictionary = {
    "a": path_a(),
    "b": path_b(),
    "k": path_k(),
    }
    
def drawLetterPaths(txt):
    cursor = 0
    scale(.85)
    translate(20, 160)
    for char in txt:
        print char
        letter = fontPathDictionary.get(char) # missing_glyph())
        
        print letter[0]
       
        for stroke in letter[0]:
            drawStroke(stroke[0],stroke[1],stroke[2],stroke[3])
            
        if cursor > 200:
            cursor = 0
            translate(-240, -290)
            print "cursor is " + str(cursor)
        else:
            translate(letter[1],0)
            cursor += letter[1]
            print "cursor is " + str(cursor)
        

        
drawLetterPaths("kabk")

# frameNum = 20
# lineThickness = frameNum

# for frame in range(frameNum):
#     newPage(1000,1000)
#     fill(0,0,1)
#     rect(0,0,1000,1000)
#     fill(1,1,1)
#     translate(54, -316)
#     scale(3)
#     lineThickness = frameNum*cos(frame*.25+10)
#     path_k()

# saveImage("../exports/gifs/blockletter-k-6-111717.gif")


# to use this pen tool on bezier paths, the math looks like...
# x1,y1 = P1
# x2,y2 = P2
# x3,y3 = P3
# x4,y4 = P4
# x = x1*(1-t)**3 + x2*3*t*(1-t)**2 + x3*3*t**2*(1-t) + x4*t**3
# y = y1*(1-t)**3 + y2*3*t*(1-t)**2 + y3*3*t**2*(1-t) + y4*t**3

