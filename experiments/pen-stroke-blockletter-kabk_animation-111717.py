newPage(500,500)

lineThickness = 3


def drawStoke(pointA,pointB,angle, strokeWidth):
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
    # print int(floor(divisions))
    
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
    letterWidth = 200
    drawStoke((132, 344), (106, 210), 205, 46)
    drawStoke((126, 162), (46, 186), 45, 46)
    drawStoke((164, 377), (238, 372), 65, 46)
    drawStoke((210, 340), (246, 214), 205, 46)
    drawStoke((210, 186), (272, 174), 45, 46)
    drawStoke((154, 276), (188, 256), 45, 46)
    return letterWidth       

def path_b():
    letterWidth = 200
    drawStoke((70, 392), (106, 210), 205, 46)
    drawStoke((46, 180), (182, 176), 57, 46)
    drawStoke((114, 374), (216, 394), 57, 46)
    drawStoke((228, 375), (161, 320), 186, 46)
    drawStoke((128, 296), (224, 290), 57, 46)
    drawStoke((236, 271), (218, 200), 8, 46)
    return letterWidth        

def path_k():
    letterWidth = 200
    drawStoke((76, 346), (106, 210), 221, 46)
    drawStoke((308, 160), (46, 186), 45, 46)
    drawStoke((176, 384), (104, 382), 65, 46)
    drawStoke((133, 260), (216, 222), 54, 46)
    drawStoke((152, 300), (236, 302), 76, 44)
    drawStoke((193, 182), (244, 171), 65, 46)
    return letterWidth
    

# path_a()

path_b()

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

