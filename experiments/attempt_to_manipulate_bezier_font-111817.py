bezReg = BezierPath()
bezReg.text("D", font="InputSans-Bold", fontSize=700, offset=(100,100))

# print bezReg.getNSBezierPath()
# print bezReg.points

# bez = bezReg.skew(1)

fill(1,0,0)
stroke(0)
strokeWidth(10)
# drawPath(bezReg)
# for contour in bezReg.contours:
#     for segment in contour:
#         for x, y in segment:
#             print x, y

# drawPath(bezReg)

# for point in bezReg:
#     translate(randint(2,500),randint(2,500))
        
def move_a_lot_of_points_at_once(x,y,points):
    # newBez = BezierPath()
    # print bezReg.points
    # newPoints = []
    
    counter = 0
    # print bezReg.points[counter]
    
    # for px, py in points:
    # for i in range(len(points) - 0):
    for px, py in points:
        print "counter is " + str(counter)
        print bezReg.points[counter]
        # bezReg.points[counter] = (px+randint(-50, 50)*x, py+randint(-50, 50)*y)
        bezReg.points[counter] = (0,0)
        print bezReg.points[counter]
        # if counter < len(points):
        #     bezReg.points[counter] = (px+randint(-50, 50)*x, py+randint(-50, 50)*y)
        #     print bezReg.points[counter]
        counter += 1
        # for px, py in points:
        #     if counter < len(points):
        #         bezReg.points[counter] = (px+randint(-50, 50)*x, py+randint(-50, 50)*y)
        #         print bezReg.points[counter]
            
    # print newPoints
    # drawPath(newPoints)
    # print newPoints
    # bezReg.points = newPoints
    drawPath(bezReg)
    
    # bezReg.points = bezReg.points._replace(v=node.v)
    # return BezierPath(newPoints)
        
# bez = move_a_lot_of_points_at_once(30,20,bezReg.points)
print bezReg.points[-1]

def replaceItem(listItem):
    listItem = (1000.0, 1000.0)
    drawPath(bezReg)
    # print "n".join(str(bezReg.getNSBezierPath()))
    print type(bezReg.getNSBezierPath())
    return listItem

# foo[1] = (foo[1][0], "friend")
print replaceItem(bezReg.points[1])
# drawPath(bezReg)
