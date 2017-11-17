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
            
print "hello"