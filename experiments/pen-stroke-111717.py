newPage(500,500)

lineThickness = 10


def drawStoke(pointA,pointB,angle, strokeWidth):
    # rect with pointA as center, rotated to angle
    save()
    translate(pointA[0],pointA[1])
    rotate(angle)
    translate(-pointA[0],-pointA[1])
    fill(0.8,0.8,1)
    # rect(0,0,500,500)
    fill(0,0,1)
    rect(pointA[0]-strokeWidth/2, pointA[1]-lineThickness/2, strokeWidth,lineThickness)
    restore()
    
    save()
    translate(pointB[0],pointB[1])
    rotate(angle)
    translate(-pointB[0],-pointB[1])
    rect(pointB[0]-strokeWidth/2, pointB[1]-lineThickness/2, strokeWidth,lineThickness)
    restore()
    # rect with pointB as center, rotated to angle
    # rects posititioned between pointA and pointB, with center points interpolated with a divisor of
        # distance pointA - pointB divided by strokeDistance
        
        
drawStoke((200, 352), (294, 126), 26, 260)